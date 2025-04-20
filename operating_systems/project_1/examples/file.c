/**
 * \file file.c
 * \author Aggelos Kolaitis <neoaggelos@gmail.com>
 * \date 2020-03-02
 * \short Read from file "in.txt" and write to stderr
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>

/* File Descriptors for stdin and stdout */
#define FD_STDIN 0
#define FD_STDOUT 1
#define FD_STDERR 2

/* Arbitrary buffer size */
#define BUFFER_SIZE 64

/* User read-write, group read, others read */
#define PERMS 0644

/**
 * Program entry point.
 */
int main(int argc, char **argv)
{
    int n_read, n_write;
    char buffer[BUFFER_SIZE];

    // Open file for reading
    int fd_in = open("in.txt", O_RDONLY);
    if (fd_in == -1)
    {
        perror("open");
        exit(-1);
    }

    do
    {
        // Read at most BUFFER_SIZE bytes, returns number of bytes read
        n_read = read(fd_in, buffer, BUFFER_SIZE);
        if (n_read == -1)
        {
            perror("read");
            exit(-1);
        }

        // Write at most n_read bytes (why?), returns number of bytes written
        n_write = write(FD_STDERR, buffer, n_read);
        if (n_write < n_read)
        {
            perror("write");
            exit(-1);
        }
    } while (n_read > 0); // (why?)

    // Close input file
    close(fd_in);
}
