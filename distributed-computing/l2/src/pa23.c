#include "./workers.h"
#include "banking.h"


int main(int argc, char* argv[]) {
  if (argc < 3 || strlen(argv[1]) != 2 || strncmp(argv[1], "-p", 2) != 0) {
    fprintf(stderr, "use with `-p X`, where X is the number of processes\n");
    return 1;
  }

  int num;
  int result = sscanf(argv[2], "%d", &num);

  if (result != 1) {
    fprintf(stderr, "Conversion failed for string \"%s\"\n", argv[2]);
    return 1;
  }
  if (num < 1 || num > MAX_PROCESS_ID) {
    fprintf(stderr, "X must be in range 1..10, but got: %d\n", num);
    return 1;
  }

  int S[MAX_PROCESS_ID];
  for (int i = 0; i < num; ++i) {
    int num;
    int result = sscanf(argv[i + 3], "%d", &num);

    if (result != 1) {
      fprintf(stderr, "Conversion failed for string \"%s\"\n", argv[2]);
      return 1;
    }
    if (num < 1 || num > 100) {
      fprintf(stderr, "S must be in range 1..100, but got: %d\n", num);
      return 1;
    }
    S[i] = num;
  }

  return main_worker(num, S);
}
