# operating_systems

A repository containing all the solutions of the Operating Systems ECE NTUA Course.


## Useful System Calls

### open

Opens a specified file.

> `int open(const char *pathname, int flags, mode_t mode)`

> - *pathname*: the filepath specified.
> - *flags*: a bitwise-or of some flags to specify create/open/operation effects.
> - *mode*: optional, specifies the user permissions on the file if created by open. 
> - **returns**: int file descriptor, reference to the file.

### close 

Closes a specified file.

> `int close(int fd)`

> - *fd*: the file descriptor, reference to the file.
> - **returns**: int, 0 on success, -1 on failure.

### read 

Reads from a file.

> `ssize_t read(int fd, void *buf, size_t count)`

> - *fd*: the file descriptor, reference to the file.
> - *buf*: the buffer to write data to.
> - *count*: the maximum amount of bytes to write to buf.
> - **returns**: ssize_t, on success the amount of bytes read as well as the file position is advanced by this amount, on failure -1.

### write 

Writes to a file.

> `ssize_t write(int fd, void *buf, size_t count)`

> - *fd*: the file descriptor, reference to the file.
> - *buf*: the buffer to read data from.
> - *count*: the maximum amount of bytes to write into fd.
> - **returns**: ssize_t, on success the amount of bytes written, on failure -1.

### perror

Prints a message to stderr.

> `void perror(const char *str)`

### exit

Terminates the calling process immediatebly.

> `void exit(int status)`

### fork

Create a child process and returns the child PID to the parent and 0 to the child.

> `pid_t fork()`

### getpid

Returns the PID of the calling process.

> `pid_t getpid()`

### getppid

Returns the PID of the parent of the calling process.

> `pid_t getppid()`

### wait

Wait for any child process to change state.

> `pid_t wait(int *wstatus)`

### waitpid

Wait for a specific child process to change state.

> `pid_t waitpid(pid_t pid, int *wstatus, int options)`

### execv

Replaces the current process image with a new one.

> `int execv(const char *path, char * const argv[])`

## Common File Descriptors

- stdin :   0
- stdout :  1
- stderr :  2
