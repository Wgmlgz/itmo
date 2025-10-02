#include "ipc.h"

#include "nig.h"

int send(void* self, local_id dst, const Message* msg) {
  return nig_send((Nig*)(self), dst, msg);
}

int send_multicast(void* self, const Message* msg) {
  return nig_send_multicast((Nig*)(self), msg);
}

int receive(void* self, local_id from, Message* msg) {
  return nig_receive((Nig*)(self), from, msg);
}

int receive_any(void* self, Message* msg) {
  return nig_receive_any((Nig*)(self), msg);
}

int request_cs(const void* self) { return nig_request_cs((Nig*)(self)); }

int release_cs(const void* self) { return nig_release_cs((Nig*)(self)); }
