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
#include "./pa2345.h"
#include "banking.h"
#include "common.h"

int main_worker(int num);
int child_worker(Nig* nig, local_id id, pid_t pid, pid_t parent_pid, int other,
                 int balance);

void tracker_sync_history(Nig* self) {
  int cur = get_lamport_time();
  for (int t = self->history.s_history_len; t <= cur; ++t) {
    memcpy(&self->history.s_history[t], &self->state, sizeof(BalanceState));
    self->history.s_history[t].s_time = t;
  }
  self->history.s_history_len = cur + 1;
  self->history.s_history[cur].s_balance = self->state.s_balance;
}

int nig_continue(Nig* nig, Message* msg) {
  local_id id;
  int res = nig_receive_any_with_id(nig, msg, &id);
  if (res == 0) {
    if (msg->s_header.s_type == STARTED) {
      nig->r_started++;
    } else if (msg->s_header.s_type == DONE) {
      nig->r_done++;
    } else if (msg->s_header.s_type == STOP) {
      nig->r_stop++;
    } else if (msg->s_header.s_type == CS_RELEASE) {
      nig_erase(nig, id);
    } else if (msg->s_header.s_type == CS_REQUEST) {
      Message buff;
      nig_enqueue(nig, msg->s_header.s_local_time, id);
      msg_set_str(&buff, CS_REPLY, "");
      nig_send(nig, id, &buff);
    }
  }
  return res;
}

int nig_request_cs(Nig* self) {
  Message msg;
  // printf("huh?....\n");

  msg_set_str(&msg, CS_REQUEST, "");
  nig_enqueue(self, msg.s_header.s_local_time, self->self_id);
  nig_send_multicast(self, &msg);

  self->m_got = 0;
  // printf("pending....\n");
  while (1) {
    int res = nig_continue(self, &msg);
    if (res != 0) continue;
    if (msg.s_header.s_type == CS_REPLY) self->m_got++;
    if (self->m_got == (self->processes - 1) &&
        self->m_queue[0].id == self->self_id) {
      break;
    }
  }

  // printf("request granted\n");
  return 0;
}

int nig_release_cs(Nig* self) {
  nig_erase(self, self->self_id);
  Message msg;
  msg_set_str(&msg, CS_RELEASE, "");
  nig_send_multicast(self, &msg);
  return 0;
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
    int res = nig_continue(self, &msg);
    if (res != 0) continue;
    if (msg.s_header.s_type == ACK) {
      // printf("ack, recieved\n");
      break;
    }
  }
}

int main_worker(int num) {
  log_fd = open(events_log, O_WRONLY | O_CREAT | O_APPEND, 0644);

  pid_t parent_pid = getpid();

  Nig nig = nig_new(num + 1);
  // spawn workers
  for (local_id i = 1; i <= num; ++i) {
    pid_t p = fork();
    if (p < 0) {
      err(EXIT_FAILURE, "fork fail");
    } else if (p == 0) {
      return child_worker(&nig, i, getpid(), parent_pid, num - 1, 0);
    }
  }

  // main settup
  nig_set_self(&nig, 0, PARENT_ID);
  Message msg;

  // wait for r_started from all children
  while (1) {
    nig_continue(&nig, &msg);
    if (nig.r_started == num) break;
  }
  logger(log_received_all_started_fmt, get_lamport_time(), PARENT_ID);

  // main work

  // printf("robbery r_done\n");

  while (1) {
    nig_continue(&nig, &msg);
    if (nig.r_done == num) break;
  }
  logger(log_received_all_done_fmt, get_lamport_time(), PARENT_ID);

  // while (1) {
  //   nig_continue(&nig, &msg);
  //   if (nig.all_history.s_history_len == num) {
  //     break;
  //   }
  // }
  // wait for all children
  pid_t wpid;
  int status = 0;
  while ((wpid = wait(&status)) > 0);
  // print_history(&nig.all_history);
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
    nig_continue(nig, &msg);
    if (nig->r_started == other) break;
  }
  logger(log_received_all_started_fmt, get_lamport_time(), id);

  // actual work

  // printf("starging work...\n");

  for (int i = 1; i <= id * 5; ++i) {
    if (use_m) nig_request_cs(nig);
    snprintf(buff, 255, log_loop_operation_fmt, id, i, id * 5);
    print(buff);
    if (use_m) nig_release_cs(nig);
  }
  // printf("%d sratring work\n", id);

  // while (1) {
  //   nig_continue(nig, &msg);
  //   // printf("%d, %d, %d\n", tracker.r_started, tracker.r_done,
  //   // tracker.r_stop);
  //   if (nig->r_stop > 0) break;
  // }
  // printf("%d r_stop recieved\n", id);

  // send r_done
  snprintf(buff, 255, log_done_fmt, get_lamport_time(), id,
           nig->state.s_balance);
  logger("%s", buff);
  send_multicast(nig, msg_set_str(&msg, DONE, buff));

  // wait for others r_done
  while (1) {
    nig_continue(nig, &msg);
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
