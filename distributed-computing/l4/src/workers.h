#ifndef WORKERS_H
#define WORKERS_H

#include <err.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#include "./nig.h"
// #include "./pa1.h"
#include "./pa2345.h"
#include "banking.h"
#include "common.h"

int main_worker(int num, int* S);
int child_worker(Nig* nig, local_id id, pid_t pid, pid_t parent_pid, int other,
                 int balance);

// Tracker new_tracker(local_id id, int balance) {
//   Tracker tracker;
//   tracker.r_started = 0;
//   tracker.r_done = 0;
//   tracker.r_stop = 0;

//   tracker.state.s_balance = balance;
//   tracker.state.s_balance_pending_in = 0;
//   tracker.state.s_time = 0;

//   tracker.history.s_id = id;
//   tracker.history.s_history_len = 0;

//   tracker.all_history.s_history_len = 0;
//   return tracker;
// }

void tracker_sync_history(Nig* self) {
  int cur = get_lamport_time();
  for (int t = self->history.s_history_len; t <= cur; ++t) {
    memcpy(&self->history.s_history[t], &self->state, sizeof(BalanceState));
    self->history.s_history[t].s_time = t;
  }
  self->history.s_history_len = cur + 1;
  self->history.s_history[cur].s_balance = self->state.s_balance;
}

int tracker_continue(Nig* nig, Message* msg) {
  int res = nig_receive_any(nig, msg);
  if (res == 0) {
    if (msg->s_header.s_type == STARTED) {
      nig->r_started++;
    } else if (msg->s_header.s_type == DONE) {
      nig->r_done++;
    } else if (msg->s_header.s_type == STOP) {
      nig->r_stop++;
    } else if (msg->s_header.s_type == TRANSFER) {
      TransferOrder order;
      memcpy(&order, msg->s_payload, sizeof(TransferOrder));
      if (order.s_src == nig->self_id) {
        // Build outgoing message first: this advances Lamport once and stamps ts_send
        Message fwd;
        msg_set_sized(&fwd, TRANSFER, &order, sizeof(TransferOrder));
        timestamp_t ts_send = fwd.s_header.s_local_time;

        // Align history to ts_send, apply balance change at ts_send
        for (int t = nig->history.s_history_len; t <= ts_send; ++t) {
          memcpy(&nig->history.s_history[t], &nig->state, sizeof(BalanceState));
          nig->history.s_history[t].s_time = t;
        }
        if (nig->history.s_history_len <= ts_send)
          nig->history.s_history_len = ts_send + 1;

        nig->state.s_balance -= order.s_amount;
        tracker_sync_history(nig);

        logger(log_transfer_out_fmt, ts_send, order.s_src, order.s_amount, order.s_dst);
        nig_send(nig, order.s_dst, &fwd);
      } else if (order.s_dst == nig->self_id) {
        // On receive, we already merged Lamport with msg ts in receive()
        // Backfill pending incoming between send ts and receive ts-1
        timestamp_t ts_send = msg->s_header.s_local_time;
        timestamp_t ts_recv = get_lamport_time();
        if (ts_send < 0) ts_send = 0;
        if (ts_recv < 0) ts_recv = 0;
        // Ensure history up to ts_recv exists
        for (int t = nig->history.s_history_len; t <= ts_recv; ++t) {
          memcpy(&nig->history.s_history[t], &nig->state, sizeof(BalanceState));
          nig->history.s_history[t].s_time = t;
        }
        if (nig->history.s_history_len <= ts_recv)
          nig->history.s_history_len = ts_recv + 1;
        for (int t = ts_send; t < ts_recv; ++t) {
          if (t >= 0 && t <= MAX_T) {
            nig->history.s_history[t].s_balance_pending_in += order.s_amount;
          }
        }
        // Apply the incoming balance at ts_recv
        nig->state.s_balance += order.s_amount;
        tracker_sync_history(nig);

        logger(log_transfer_in_fmt, ts_recv, order.s_dst, order.s_amount, order.s_src);

        Message ack_msg;
        msg_set_str(&ack_msg, ACK, "");
        nig_send(nig, PARENT_ID, &ack_msg);
      }
    } else if (msg->s_header.s_type == BALANCE_HISTORY) {
      memcpy(&nig->all_history.s_history[nig->all_history.s_history_len],
             msg->s_payload, sizeof(BalanceHistory));
      ++nig->all_history.s_history_len;
    }
  }
  return res;
}

void transfer(void* parent_data, local_id src, local_id dst, balance_t amount) {
  Nig* self = (Nig*)(parent_data);

  TransferOrder order;
  order.s_amount = amount;
  order.s_src = src;
  order.s_dst = dst;

  Message msg;
  msg_set_sized(&msg, TRANSFER, &order, sizeof(TransferOrder));
  nig_send(self, src, &msg);
  while (1) {
    int res = tracker_continue(self, &msg);
    if (res != 0) continue;
    if (msg.s_header.s_type == ACK) {
      // printf("ack, recieved\n");
      break;
    }
  }
}

int main_worker(int num, int* S) {
  log_fd = open(events_log, O_WRONLY | O_CREAT | O_APPEND, 0644);

  pid_t parent_pid = getpid();

  Nig nig = nig_new(num + 1);
  // spawn workers
  for (local_id i = 1; i <= num; ++i) {
    pid_t p = fork();
    if (p < 0) {
      err(EXIT_FAILURE, "fork fail");
    } else if (p == 0) {
      return child_worker(&nig, i, getpid(), parent_pid, num - 1, S[i - 1]);
    }
  }

  // main settup
  nig_set_self(&nig, 0, PARENT_ID);
  Message msg;

  // wait for r_started from all children
  while (1) {
    tracker_continue(&nig, &msg);
    if (nig.r_started == num) break;
  }
  logger(log_received_all_started_fmt, get_lamport_time(), PARENT_ID);

  // main work
  bank_robbery(&nig, num);
  send_multicast(&nig, msg_set_str(&msg, STOP, ""));

  // printf("robbery r_done\n");

  while (1) {
    tracker_continue(&nig, &msg);
    if (nig.r_done == num) break;
  }
  logger(log_received_all_done_fmt, get_lamport_time(), PARENT_ID);

  while (1) {
    tracker_continue(&nig, &msg);
    if (nig.all_history.s_history_len == num) {
      break;
    }
  }
  // wait for all children
  pid_t wpid;
  int status = 0;
  while ((wpid = wait(&status)) > 0);
  print_history(&nig.all_history);
  return 0;
}

int child_worker(Nig* nig, local_id id, pid_t pid, pid_t parent_pid, int other,
                 int balance) {
  // init
  nig_set_self(nig, balance, id);
  Message msg;
  char buff[255];

  // send start
  snprintf(buff, 255, log_started_fmt, get_lamport_time(), id, pid, parent_pid,
           balance);
  logger("%s", buff);
  send_multicast(nig, msg_set_str(&msg, STARTED, buff));

  // wait for others start
  while (1) {
    tracker_continue(nig, &msg);
    if (nig->r_started == other) break;
  }
  logger(log_received_all_started_fmt, get_lamport_time(), id);

  // actual work
  // printf("%d sratring work\n", id);

  while (1) {
    tracker_continue(nig, &msg);
    // printf("%d, %d, %d\n", tracker.r_started, tracker.r_done,
    // tracker.r_stop);
    if (nig->r_stop > 0) break;
  }
  // printf("%d r_stop recieved\n", id);

  // send r_done
  snprintf(buff, 255, log_done_fmt, get_lamport_time(), id,
           nig->state.s_balance);
  logger("%s", buff);
  send_multicast(nig, msg_set_str(&msg, DONE, buff));

  // wait for others r_done
  while (1) {
    tracker_continue(nig, &msg);
    if (nig->r_done == other) break;
  }
  logger(log_received_all_done_fmt, get_lamport_time(), id);

  tracker_sync_history(nig);
  send(nig, PARENT_ID,
       msg_set_sized(&msg, BALANCE_HISTORY, &nig->history,
                     sizeof(BalanceHistory)));
  return 0;
}

#endif
