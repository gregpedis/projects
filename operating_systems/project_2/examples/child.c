/**
 * \file child.c
 * \author Aggelos Kolaitis <neoaggelos@gmail.com>
 * \date 2021-03-26
 * \brief execv() example, child process.
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv) {
  printf("Child process %d\n", getpid());

  printf("Called with arguments: %s", argv[0]);
  for (int i = 1; i < argc; i++) {
    printf(" %s", argv[1]);
  }
  printf("\n");

  return 0;
}
