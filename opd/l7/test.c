#include <stdio.h>

#define BYTE_TO_BINARY_PATTERN "%c%c%c%c%c%c%c%c"
#define BYTE_TO_BINARY(byte)  \
  ((byte) & 0x80 ? '1' : '0'), \
  ((byte) & 0x40 ? '1' : '0'), \
  ((byte) & 0x20 ? '1' : '0'), \
  ((byte) & 0x10 ? '1' : '0'), \
  ((byte) & 0x08 ? '1' : '0'), \
  ((byte) & 0x04 ? '1' : '0'), \
  ((byte) & 0x02 ? '1' : '0'), \
  ((byte) & 0x01 ? '1' : '0') 
int main() {
  int x = -1;
  int t = x;
  printf(BYTE_TO_BINARY_PATTERN"\n", BYTE_TO_BINARY(t));
  t <<= 1;
  t += x;
  t <<= 1;
printf(BYTE_TO_BINARY_PATTERN"\n", BYTE_TO_BINARY(t));
  printf("%d\n", t);
}