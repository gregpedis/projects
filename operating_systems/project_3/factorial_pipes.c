#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <time.h>

#define DEFAULT "\033[30;1m"
#define RED "\033[31;1m"
#define GREEN "\033[32m"
#define YELLOW "\033[33m"
#define BLUE "\033[34m"
#define MAGENTA "\033[35m"
#define CYAN "\033[36m"
#define WHITE "\033[37m"
#define GRAY "\033[38;1m"

#define CHLD_MESSAGE_CURRENT "[Child=%d] %d * %d = %d"
#define CHLD_MESSAGE_EXITING_RESULT "[Child=%d] Finished my job. RESULT: %d."
#define CHLD_MESSAGE_EXITING "[Child=%d] Finished my job. I'm going home!"

#define PRNT_MESSAGE_INITIAL "[PARENT] Initiating factorial of %d with %d processes"
#define PRNT_MESSAGE_FINAL "[PARENT] All children exited, terminating as well"

#define WAIT_TIME 1

int **pipe_fds;

void alloc_pipes(int pipe_count)
{
    pipe_fds = (int **)malloc(sizeof(int *) * pipe_count);

    for (size_t i = 0; i < pipe_count; i++)
    {
        pipe_fds[i] = (int *)malloc(sizeof(int) * 2);
        if (pipe(pipe_fds[i]) == -1)
        {
            perror("Failed at creating a pipe.");
            exit(EXIT_FAILURE);
        }
    }
}

void free_pipes(int process_count)
{
    for (size_t i = 0; i < process_count; i++)
    {
        free(pipe_fds[i]);
    }

    free(pipe_fds);
}

void do_child_work(int orderId, int process_count, int target)
{
    int old_value, new_value;
    char read_buffer[80], write_buffer[80];

    int current_multiplier = orderId + 1;
    int readFrom = orderId;
    int writeTo = (orderId + 1 == process_count) ? 0 : orderId + 1;

    while (target >= current_multiplier)
    {
        read(pipe_fds[readFrom][0], read_buffer, sizeof(read_buffer));
        sscanf(read_buffer, "%d", &old_value);

        sleep(WAIT_TIME);

        new_value = old_value * current_multiplier;
        printf(YELLOW CHLD_MESSAGE_CURRENT DEFAULT "\n", orderId, old_value, current_multiplier, new_value);

        if (current_multiplier == target)
        {
            printf(GREEN CHLD_MESSAGE_EXITING_RESULT DEFAULT "\n", orderId, new_value);
            exit(EXIT_SUCCESS);
        }

        sprintf(write_buffer, "%d", new_value);
        write(pipe_fds[writeTo][1], write_buffer, sizeof(write_buffer));

        current_multiplier += process_count;

        sleep(WAIT_TIME);
    }

    printf(GRAY CHLD_MESSAGE_EXITING DEFAULT "\n", orderId);
    exit(EXIT_SUCCESS);
}

void do_parent_work(int process_count, int target)
{
    //*(*pipe_fds + 1)
    write(pipe_fds[0][1], "1", 2);

    int n = process_count;
    while (n > 0)
    {
        int status;
        wait(&status);
        n--;
    }

    free_pipes(process_count);
    printf(MAGENTA PRNT_MESSAGE_FINAL DEFAULT "\n");
    exit(EXIT_SUCCESS);
}

void do_some_forks(int process_count, int target)
{
    printf(MAGENTA "Forking baby!" DEFAULT "\n");
    for (int i = 0; i < process_count; i++)
    {
        pid_t p = fork();

        if (p < 0)
        {
            perror("fork");
        }
        else if (p == 0)
        {
            do_child_work(i, process_count, target);
        }
    }
}

int main(int argc, char **argv)
{
    if (argc < 3)
    {
        perror("Not enough arguments. Please specify number of child process as well as factorial target");
        exit(EXIT_FAILURE);
    }

    int process_count = atoi(argv[1]);
    int target = atoi(argv[2]);

    if (process_count < 1)
    {
        perror("Process count must be positive");
        exit(EXIT_FAILURE);
    }

    if (target > 12)
    {
        perror("Factorial calculations can go up to 12 or we end up with nasty int overflows");
        exit(EXIT_FAILURE);
    }

    printf(MAGENTA PRNT_MESSAGE_INITIAL DEFAULT "\n", target, process_count);

    alloc_pipes(process_count);
    do_some_forks(process_count, target);

    do_parent_work(process_count, target);
    return 0;
}
