/**
 * \file fork.c
 * \author Aggelos Kolaitis <neoaggelos@gmail.com>
 * \date 2020-03-02
 * \short Example program with fork()
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * Program entry point.
 */
int main(int argc, char **argv)
{
    pid_t pid = fork();
    if (pid == -1)
    {
        perror("fork");
    }
    else if (pid == 0)
    {
        printf("CHILD: My pid is %d, my father is %d\n", getpid(), getppid());
    }
    else
    {
        printf("PARENT: My pid is %d, my father is %d\n", getpid(), getppid());
        wait(NULL);
    }
    return 0;
}
