/**
 * \file parent.c
 * \author Aggelos Kolaitis <neoaggelos@gmail.com>
 * \date 2021-03-26
 * \brief execv() example, parent process.
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * \brief If @ret is negative, print an error message and exit with EXIT_FAILURE
 * status code
 *
 * \param ret Value to check
 * \param msg Error message to prepend
 */
void check_neg(int ret, const char *msg) {
  if (ret < 0) {
    perror(msg);
    exit(EXIT_FAILURE);
  }
}

/**
 * \brief Parse result of wait() system call and print a descriptive message to
 * stdout
 *
 * Refer to `man 2 wait` for more details regarding the meaning of pid and
 * status.
 *
 * \param pid PID returned by wait()
 * \param status Status returned by wait()
 */
void describe_wait_status(pid_t pid, int status) {
  if (pid < 1) {
    perror("wait() call failed");
  }

  if (pid == 0) {
    printf("Nothing happened");
  }

  if (WIFSTOPPED(status)) {
    printf("Child with PID %d stopped\n", pid);
  } else if (WIFCONTINUED(status)) {
    printf("Child with PID %d continued\n", pid);
  } else if (WIFEXITED(status)) {
    printf("Child with PID %d exited with status code %d\n", pid,
           WEXITSTATUS(status));
  } else if (WIFSIGNALED(status)) {
    printf("Child with PID %d terminated by signal %d with status code %d\n",
           pid, WSTOPSIG(status), WEXITSTATUS(status));
  }
}

int main(int argc, char **argv) {
  pid_t p = fork();
  check_neg(p, "fork");

  if (p == 0) {
    /* child, load ./child executable */
    char *const argv[] = {"./child", "Hello", NULL};
    int status = execv("./child", argv);

    /* on success, execution will never reach this line */
    check_neg(status, "Failed to create child");
  }

  printf("Parent process, waiting for child to terminate\n");

  int status;
  pid_t pid = wait(&status);
  describe_wait_status(pid, status);
  return 0;
}
