#include <getopt.h>
#include "./workers.h"
#include "banking.h"

int main(int argc, char* argv[]) {
  int num = 0;
  int p_provided = 0;

  static struct option long_options[] = {
    {"mutexl", no_argument, NULL, 'm'},
    {NULL, 0, NULL, 0}
  };

  int opt;
  while ((opt = getopt_long(argc, argv, "p:", long_options, NULL)) != -1) {
    switch (opt) {
      case 'p': {
        p_provided = 1;
        int result = sscanf(optarg, "%d", &num);
        if (result != 1) {
          fprintf(stderr, "Conversion failed for string \"%s\"\n", optarg);
          return 1;
        }
        break;
      }
      case 'm':
        use_m = 1;
        break;
      case '?':
        // getopt_long already prints error for unknown options or missing args
        return 1;
    }
  }

  if (!p_provided) {
    fprintf(stderr, "use with `-p X`, where X is the number of processes\n");
    return 1;
  }

  if (num < 1 || num > MAX_PROCESS_ID) {
    fprintf(stderr, "X must be in range 1..10, but got: %d\n", num);
    return 1;
  }

  if (optind < argc) {
    fprintf(stderr, "Unexpected extra arguments\n");
    return 1;
  }

  return main_worker(num);
}
