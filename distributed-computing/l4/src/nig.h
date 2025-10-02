#ifndef NIG_H
#define NIG_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#include "./ipc.h"
#include "banking.h"
int log_fd;
int use_m;

typedef struct {
  timestamp_t t;
  local_id id;
} QEntry;

typedef struct {
  // from, to
  int pfd[MAX_PROCESS_ID][MAX_PROCESS_ID][2];
  local_id self_id;
  int processes;

  int r_started;
  int r_done;
  int r_stop;
  int ack;
  BalanceState state;
  BalanceHistory history;
  AllHistory all_history;


  QEntry m_queue[MAX_PROCESS_ID * 4];

  int want_cs;
  int qeueue_len;
  int m_got;

} Nig;

Nig nig_new(int processes);

Message* msg_set_sized(Message* msg, MessageType type, const void* s_payload,
                       int size);
Message* msg_set_str(Message* msg, MessageType type, const char* s_payload);
void nig_set_self(Nig* self, balance_t balance, local_id self_id);
int nig_send(Nig* self, local_id dst, const Message* msg);
int nig_send_multicast(Nig* self, const Message* msg);
int nig_receive(Nig* self, local_id from, Message* msg);
int nig_receive_any(Nig* self, Message* msg);
int nig_receive_any_with_id(Nig* self, Message* msg, local_id* id);
int nig_request_cs(Nig* self);
int nig_release_cs(Nig* self);
void nig_erase(Nig* self, local_id id);
void nig_enqueue(Nig* self, timestamp_t t, local_id id);


void logger(const char* fmt, ...);

#endif
