#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include "./workers.h"
#include "./pa1.h"


int main(int argc, char** argv) {
  if (argc < 3 || argc > 3 || strlen(argv[1]) != 2 ||
      strncmp(argv[1], "-p", 2) != 0) {
    fprintf(stderr, "use with `-p X`, where X is the number of processes\n");
    return 1;
  }

  int num;
  int result = sscanf(argv[2], "%d", &num);

  if (result != 1) {
    fprintf(stderr, "Conversion failed for string \"%s\"\n", argv[2]);
    return 1;
  }
  if (num < 1 || num > 10) {
    fprintf(stderr, "X must be in range 1..10\n");
    return 1;
  }

  return main_worker(num);
}
