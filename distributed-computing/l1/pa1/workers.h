#include <err.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <fcntl.h>

#include "./nig.h"
#include "./pa1.h"
#include "common.h"

int main_worker(int num);
int child_worker(Nig* nig, local_id id, pid_t pid, pid_t parent_pid, int other);

typedef struct {
  int started;
  int done;
} Tracker;

Tracker new_tracker() {
  Tracker tracker;
  tracker.started = 0;
  tracker.done = 0;
  return tracker;
}

void tracker_continue(Tracker* self, Nig* nig, Message* msg) {
  if (receive_any(nig, msg) != 0) return;
  if (msg->s_header.s_type == STARTED) {
    ++self->started;
  }
  if (msg->s_header.s_type == DONE) {
    ++self->done;
  }
}

int main_worker(int num) {
  log_fd = open("events.log", O_WRONLY | O_CREAT | O_APPEND, 0644);

  pid_t parent_pid = getpid();

  Nig nig = nig_new(num + 1);
  // spawn workers
  for (local_id i = 1; i <= num; ++i) {
    pid_t p = fork();
    if (p < 0) {
      err(EXIT_FAILURE, "fork fail");
    } else if (p == 0) {
      return child_worker(&nig, i, getpid(), parent_pid, num - 1);
    }
  }

  nig_set_self(&nig, PARENT_ID);
  // wait for started
  Tracker tracker = new_tracker();
  Message msg;

  while (1) {
    tracker_continue(&tracker, &nig, &msg);
    if (tracker.started == num) break;
  }
  logger(log_received_all_started_fmt, PARENT_ID);

  while (1) {
    tracker_continue(&tracker, &nig, &msg);
    if (tracker.done == num) break;
  }
  logger(log_received_all_done_fmt, PARENT_ID);

  // wait for all children
  pid_t wpid;
  int status = 0;
  while ((wpid = wait(&status)) > 0);
  return 0;
}

int child_worker(Nig* nig, local_id id, pid_t pid, pid_t parent_pid,
                 int other) {
  // init
  nig_set_self(nig, id);
  Message msg;
  Tracker tracker = new_tracker();
  char buff[255];

  // send start
  snprintf(buff, 255, log_started_fmt, id, pid, parent_pid);
  logger("%s", buff);
  send_multicast(nig, msg_new(STARTED, buff));

  // wait for others start
  while (1) {
    tracker_continue(&tracker, nig, &msg);
    if (tracker.started == other) break;
  }
  logger(log_received_all_started_fmt, id);

  // send done
  snprintf(buff, 255, log_done_fmt, id);
  logger("%s", buff);
  send_multicast(nig, msg_new(DONE, buff));

  // wait for others done
  while (1) {
    tracker_continue(&tracker, nig, &msg);
    if (tracker.done == other) break;
  }
  logger(log_received_all_done_fmt, id);
  return 0;
}
