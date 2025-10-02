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

typedef struct {
  int started;
  int done;
  int stop;
  BalanceState state;
} Tracker;

Tracker new_tracker(int balance) {
  Tracker tracker;
  tracker.started = 0;
  tracker.done = 0;
  tracker.stop = 0;

  tracker.state.s_balance = balance;
  tracker.state.s_balance_pending_in = 0;
  tracker.state.s_time = 0;
  return tracker;
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
}

int tracker_continue(Tracker* self, Nig* nig, Message* msg) {
  int res = nig_receive_any(nig, msg);
  if (res == 0) {
    if (msg->s_header.s_type == STARTED) {
      self->started++;
    } else if (msg->s_header.s_type == DONE) {
      self->done++;
    } else if (msg->s_header.s_type == STOP) {
      self->stop++;
    } else if (msg->s_header.s_type == TRANSFER) {
      TransferOrder order;
      memcpy(&order, msg->s_payload, sizeof(TransferOrder));
      if (order.s_src == nig->self_id) {
        logger(log_transfer_out_fmt, time(NULL), order.s_dst, order.s_amount,
               order.s_dst);
        self->state.s_balance -= order.s_amount;

        nig_send(nig, order.s_dst, msg);
      } else if (order.s_dst == nig->self_id) {
        logger(log_transfer_in_fmt, time(NULL), order.s_dst, order.s_amount,
               order.s_dst);
        self->state.s_balance += order.s_amount;
      }
    }
  }
  return res;
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
  nig_set_self(&nig, PARENT_ID);
  Message msg;
  Tracker tracker = new_tracker(0);

  // wait for started from all children
  while (1) {
    tracker_continue(&tracker, &nig, &msg);
    if (tracker.started == num) break;
  }
  logger(log_received_all_started_fmt, time(NULL), PARENT_ID);

  // main work
  bank_robbery(&nig, num);
  send_multicast(&nig, msg_set_str(&msg, STOP, ""));

  printf("robbery done\n");

  while (1) {
    tracker_continue(&tracker, &nig, &msg);
    if (tracker.done == num) break;
  }
  logger(log_received_all_done_fmt, time(NULL), PARENT_ID);

  // wait for all children
  pid_t wpid;
  int status = 0;
  while ((wpid = wait(&status)) > 0);
  return 0;
}

int child_worker(Nig* nig, local_id id, pid_t pid, pid_t parent_pid, int other,
                 int balance) {
  // init
  nig_set_self(nig, id);
  Message msg;
  Tracker tracker = new_tracker(balance);
  char buff[255];

  // send start
  snprintf(buff, 255, log_started_fmt, time(NULL), id, pid, parent_pid,
           balance);
  logger("%s", buff);
  send_multicast(nig, msg_set_str(&msg, STARTED, buff));

  // wait for others start
  while (1) {
    tracker_continue(&tracker, nig, &msg);
    if (tracker.started == other) break;
  }
  logger(log_received_all_started_fmt, time(NULL), id);

  // actual work
  printf("%d sratring work\n", id);

  while (1) {
    tracker_continue(&tracker, nig, &msg);
    // printf("%d, %d, %d\n", tracker.started, tracker.done, tracker.stop);
    if (tracker.stop > 0) break;
  }
  printf("%d stop recieved\n", id);

  // send done
  snprintf(buff, 255, log_done_fmt, time(NULL), id, tracker.state.s_balance);
  logger("%s", buff);
  send_multicast(nig, msg_set_str(&msg, DONE, buff));

  // wait for others done
  while (1) {
    tracker_continue(&tracker, nig, &msg);
    if (tracker.done == other) break;
  }
  logger(log_received_all_done_fmt, time(NULL), id);
  return 0;
}

#endif
