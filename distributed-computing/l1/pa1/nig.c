#include "./nig.h"

#include <err.h>
#include <stdarg.h>
#include <stdio.h>
#include <sys/ioctl.h>

#include "./common.h"
int log_fd = -1;


Nig nig_new(int processes) {
  if (processes > MAX_PROCESS_ID) {
    err(EXIT_FAILURE, "requested more then max processes");
  }

  Nig nig;
  nig.self_id = PARENT_ID;
  nig.processes = processes;

  FILE* pipes_fd = fopen(pipes_log, "w");

  for (int i = 0; i < processes; ++i) {
    for (int j = 0; j < processes; ++j) {
      if (i == j) continue;
      int res = pipe(nig.pfd[i][j]);
      if (res != 0) {
        err(EXIT_FAILURE, "failed to open pipe");
      }
      fprintf(pipes_fd, "%d read\n", nig.pfd[i][j][0]);
      fprintf(pipes_fd, "%d write\n", nig.pfd[i][j][1]);
    }
  }
  fclose(pipes_fd);

  return nig;
}

void nig_set_self(Nig* self, local_id self_id) {
  self->self_id = self_id;

  for (int i = 0; i < self->processes; ++i) {
    for (int j = 0; j < self->processes; ++j) {
      if (i == j) continue;
        if (self_id != j) {
            close(self->pfd[i][j][0]);
        }
        if (self_id != i) {
            close(self->pfd[i][j][1]);
        }
    }
  }
}

Message* msg_new(MessageType type, const char* s_payload) {
  Message* msg = (Message*)(malloc(sizeof(Message)));
  memset(msg, 0, sizeof(Message));

  msg->s_header.s_magic = MESSAGE_MAGIC;
  msg->s_header.s_payload_len = strlen(s_payload);
  msg->s_header.s_type = type;
  msg->s_header.s_local_time = time(NULL);

  strncpy(msg->s_payload, s_payload, MAX_PAYLOAD_LEN);

  return msg;
}

void msg_print(const Message* msg) {
  // printf("DBG msg: `%d`\n", msg->s_header.s_type);
}

int nig_send(Nig* self, local_id dst, const Message* msg) {
  msg_print(msg);
  if (write(self->pfd[self->self_id][dst][1], msg, sizeof(Message)) !=
      sizeof(Message))
    return 1;
  return 0;
}
int nig_send_multicast(Nig* self, const Message* msg) {
  for (int i = 0; i < self->processes; ++i) {
    if (i == self->self_id) continue;
    if (nig_send(self, i, msg) != 0) return -1;
  }
  return 0;
}
int nig_receive(Nig* self, local_id from, Message* msg) {
  int res = read(self->pfd[from][self->self_id][0], msg, sizeof(Message));

  if (res == sizeof(Message)) {
    msg_print(msg);
    return 0;
  } else {
    err(EXIT_FAILURE, "read");
  }
}
int nig_receive_any(Nig* self, Message* msg) {
  for (int i = 0; i < self->processes; ++i) {
    if (i == self->self_id) continue;
    int fd = self->pfd[i][self->self_id][0];
    int nbytes;
    if (ioctl(fd, FIONREAD, &nbytes) == -1) {
      return -1;
    }

    if (nbytes < sizeof(Message)) continue;

    return nig_receive(self, i, msg);
  }
  return -1;
}

void logger(const char* format, ...) {
  char buffer[4096];
  va_list args;
  va_start(args, format);
  int len = vsnprintf(buffer, sizeof(buffer), format, args);
  va_end(args);

  if (len < 0 || len >= sizeof(buffer)) {
      const char* err_msg = "Log message too long or error occurred\n";
      write(STDOUT_FILENO, err_msg, strlen(err_msg));
      write(log_fd, err_msg, strlen(err_msg));
      return;
  }

  write(log_fd, buffer, len);
  write(STDOUT_FILENO, buffer, len);
}

