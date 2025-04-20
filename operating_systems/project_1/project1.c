#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <string.h>
#include <fcntl.h>
#include <time.h>

#define WAIT_TIME 1

void create_file(char *filename)
{
    int fd = open(filename, O_TRUNC | O_CREAT, S_IRUSR | S_IRGRP | S_IROTH | S_IWUSR);
    close(fd);
}

void print_file(char *filename)
{

    struct stat st;
    stat(filename, &st);
    char *buffer = malloc(st.st_size);

    int fd = open(filename, O_RDONLY);
    read(fd, buffer, st.st_size);
    printf(buffer);

    free(buffer);
    close(fd);
}

void do_parent_stuff(char *filename, int target_number)
{
    for (int i = 0; i < target_number; i++)
    {
        printf("[Parent] Heartbeat PID=%d Time=%d\n", getpid(), time(NULL));
        sleep(WAIT_TIME);
    }

    pid_t wait_pid;
    int wait_status = 0;

    while ((wait_pid = wait(&wait_status)) > 0)
    {
        printf("[Parent] Child with PID=%d terminated.\n", wait_pid);
    }

    printf("[Parent] PID=%d reading file:\n", getpid());
    print_file(filename);
}

void do_child_stuff(char *filename, int target_number, int child_id, int show_even)
{
    printf("[Child%d] Started. PID=%d PPID=%d\n", child_id, getpid(), getppid());

    int fd = open(filename, O_RDWR | O_APPEND);
    const char *message = "message from %d\n";
    int length = snprintf(NULL, 0, message, getpid());
    char *str = malloc(length + 1);
    snprintf(str, length + 1, message, getpid());

    for (int i = 0; i < target_number; i++)
    {
        if ((i % 2 == 0 && show_even == 1) || (i % 2 != 0 && show_even == 0))
        {
            printf("[Child%d] Heartbeat. PID=%d Time=%d x=%d\n", child_id, getpid(), time(NULL), i);
            write(fd, str, length);
            sleep(WAIT_TIME);
        }
    }

    free(str);
    close(fd);
    printf("[Child%d] Terminating!\n", child_id);
    exit(0);
}

int main(int argc, char **argv)
{
    if (argc < 3)
    {
        printf("Please specify the filename to write to, as well as the number to count towards.\n");
        return -1;
    }

    int target_number = atoi(argv[2]);

    int fd = open(filename, O_TRUNC | O_CREAT, S_IRUSR | S_IRGRP | S_IROTH | S_IWUSR);
    printf("This is %s running\n", argv[0]);
    printf("Targeting file %s.\n", argv[1]);
    printf("Number to count towards %d.\n", target_number);

    create_file(argv[1]);

    pid_t child_a = fork();
    if (child_a == -1)
    {
        perror("wait a minute, what's this?\n");
    }
    else if (child_a == 0)
    {
        do_child_stuff(argv[1], target_number, 0, 0, fd);
    }
    else
    {
        pid_t child_b = fork();
        if (child_b == -1)
        {
            perror("wait a minute, again??\n");
        }
        else if (child_b == 0)
        {
            do_child_stuff(argv[1], target_number, 1, 1);
        }
        else
        {
            do_parent_stuff(argv[1], target_number);
        }
    }
    return 0;
}
