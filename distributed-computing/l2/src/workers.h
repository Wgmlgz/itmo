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
  int cur = get_physical_time();
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
        logger(log_transfer_out_fmt, get_physical_time(), order.s_dst,
               order.s_amount, order.s_dst);
        tracker_sync_history(nig);
        nig->state.s_balance -= order.s_amount;
        tracker_sync_history(nig);

        nig_send(nig, order.s_dst, msg);
      } else if (order.s_dst == nig->self_id) {
        tracker_sync_history(nig);
        logger(log_transfer_in_fmt, get_physical_time(), order.s_dst,
               order.s_amount, order.s_dst);
        tracker_sync_history(nig);
        nig->state.s_balance += order.s_amount;
        tracker_sync_history(nig);

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
  logger(log_received_all_started_fmt, get_physical_time(), PARENT_ID);

  // main work
  bank_robbery(&nig, num);
  send_multicast(&nig, msg_set_str(&msg, STOP, ""));

  // printf("robbery r_done\n");

  while (1) {
    tracker_continue(&nig, &msg);
    if (nig.r_done == num) break;
  }
  logger(log_received_all_done_fmt, get_physical_time(), PARENT_ID);

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
  snprintf(buff, 255, log_started_fmt, get_physical_time(), id, pid, parent_pid,
           balance);
  logger("%s", buff);
  send_multicast(nig, msg_set_str(&msg, STARTED, buff));

  // wait for others start
  while (1) {
    tracker_continue(nig, &msg);
    if (nig->r_started == other) break;
  }
  logger(log_received_all_started_fmt, get_physical_time(), id);

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
  snprintf(buff, 255, log_done_fmt, get_physical_time(), id,
           nig->state.s_balance);
  logger("%s", buff);
  send_multicast(nig, msg_set_str(&msg, DONE, buff));

  // wait for others r_done
  while (1) {
    tracker_continue(nig, &msg);
    if (nig->r_done == other) break;
  }
  logger(log_received_all_done_fmt, get_physical_time(), id);

  tracker_sync_history(nig);
  send(nig, PARENT_ID,
       msg_set_sized(&msg, BALANCE_HISTORY, &nig->history,
                     sizeof(BalanceHistory)));
  return 0;
}

#endif
