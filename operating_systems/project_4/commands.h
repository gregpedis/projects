#include "common.h"
#include "time.h"

#define CMD_GET "get"
#define CMD_HELP "help"
#define CMD_EXIT "exit"

#define BUFFER_SIZE 200
#define MSG_DEBUG_WRITE "[DEBUG] sent '%s'\n"
#define MSG_DEBUG_READ "[DEBUG] read '%s'\n"

#define MSG_SERVER_FAILURE "try again"
#define MSG_SERVER_INVALID "invalid code"

void initiate_command_loop(int sock_fd, int is_debug);

void execute_command_get(int sock_fd, int is_debug);
void execute_command_default(int sock_fd, int is_debug, char *user_input, int n_write);
void execute_command_exit(int sock_fd);
void execute_command_help();

void execute_command_loop(int sock_fd, int is_debug)
{
    if (is_debug)
    {
        printf(CLR_YELLOW "[DEBUG] Initiated command loop\n" CLR_DEFAULT);
    }

    while (1)
    {
        int n_read = 0;
        char buffer[BUFFER_SIZE];
        n_read = read(STDIN_FILENO, buffer, BUFFER_SIZE);

        // buffer[strcspn(buffer, "\n")] = 0;
        buffer[n_read - 1] = '\0';

        if (n_read < 0)
        {
            perror("read");
            exit(EXIT_FAILURE);
        }

        if (strcmp(buffer, CMD_GET) == 0)
        {
            execute_command_get(sock_fd, is_debug);
        }
        else if (strcmp(buffer, CMD_HELP) == 0)
        {
            execute_command_help();
        }
        else if (strcmp(buffer, CMD_EXIT) == 0)
        {
            execute_command_exit(sock_fd);
        }
        else
        {
            execute_command_default(sock_fd, is_debug, buffer, n_read);
        }
    }
}

void execute_command_help()
{
    printf(CLR_GRAY "\n./ask4 [--host HOST] [--port PORT] [--debug]\n\n" CLR_DEFAULT);
    printf(CLR_GRAY "--host HOST specify custom host instead of %s\n" CLR_DEFAULT, DEFAULT_HOST);
    printf(CLR_GRAY "--port PORT specify custom port instead of %d\n" CLR_DEFAULT, DEFAULT_PORT);
    printf(CLR_GRAY "--debug logs the messages of socket read/write\n\n" CLR_DEFAULT);

    printf(CLR_GRAY "> Commands available:\n\n" CLR_DEFAULT);
    printf(CLR_GRAY ">> get: fetches server state data\n" CLR_DEFAULT);
    printf(CLR_GRAY ">> help: prints this message\n" CLR_DEFAULT);
    printf(CLR_GRAY ">> exit: stop the process execution\n" CLR_DEFAULT);
    printf(CLR_GRAY ">> N name surname reason: asks for covid request\n\n" CLR_DEFAULT);
}

void execute_command_exit(int sock_fd)
{
    printf(CLR_RED "Goodbye.\n" CLR_DEFAULT);
    shutdown(sock_fd, 2);
    close(sock_fd);
    exit(EXIT_SUCCESS);
}

void execute_command_get(int sock_fd, int is_debug)
{
    char buffer[BUFFER_SIZE];

    write(sock_fd, CMD_GET, sizeof(CMD_GET));
    if (is_debug)
    {
        printf(CLR_MAGENTA MSG_DEBUG_WRITE CLR_DEFAULT, CMD_GET);
    }

    int n_read = read(sock_fd, buffer, BUFFER_SIZE);
    buffer[n_read - 1] = '\0';
    if (is_debug)
    {
        printf(CLR_MAGENTA MSG_DEBUG_READ CLR_DEFAULT, buffer);
    }

    int event_type, light_level, temperature;
    time_t timestamp;

    char time_buffer[80];
    char event_buffer[20];
    // memset(time_buffer, 0, sizeof(time_buffer));
    // memset(event_buffer, 0, sizeof(event_buffer));

    sscanf(buffer, "%d %d %d %ld", &event_type, &light_level, &temperature, &timestamp);

    switch (event_type)
    {
    case 0:
        strcpy(event_buffer, "boot");
        break;
    case 1:
        strcpy(event_buffer, "setup");
        break;
    case 2:
        strcpy(event_buffer, "interval");
        break;
    case 3:
        strcpy(event_buffer, "button");
        break;
    case 4:
        strcpy(event_buffer, "motion");
        break;
    default:
        strcpy(event_buffer, "uknown");
        break;
    }

    struct tm ts = *localtime((const time_t *)&timestamp);
    strftime(time_buffer, sizeof(time_buffer), "%Y-%m-%d %H:%M:%S", &ts);

    printf("Latest event:\n");
    printf("%s (%d)\n", event_buffer, event_type);
    printf("Temperature is: %.2f\n", temperature / 100.0f);
    printf("Light level is: %d\n", light_level);
    printf("Timestamp is: %s\n", time_buffer);
}

void execute_command_default(int sock_fd, int is_debug, char *user_input, int n_write)
{
    char read_buffer[BUFFER_SIZE];
    char write_buffer[BUFFER_SIZE];
    write(sock_fd, user_input, n_write);
    if (is_debug)
    {
        printf(CLR_MAGENTA MSG_DEBUG_WRITE CLR_DEFAULT, user_input);
    }

    int n_read = read(sock_fd, read_buffer, BUFFER_SIZE);
    read_buffer[n_read - 1] = '\0';
    if (is_debug)
    {
        printf(CLR_MAGENTA MSG_DEBUG_READ CLR_DEFAULT, read_buffer);
    }

    if (strcmp(read_buffer, MSG_SERVER_FAILURE) != 0 && strcmp(read_buffer, MSG_SERVER_INVALID) != 0)
    {
        printf("Send verification code: '%s'\n", read_buffer);
        int n_write = read(STDIN_FILENO, write_buffer, BUFFER_SIZE);
        write_buffer[n_write - 1] = '\0';
        write(sock_fd, write_buffer, n_write);

        if (is_debug)
        {
            printf(CLR_MAGENTA MSG_DEBUG_WRITE CLR_DEFAULT, write_buffer);
        }

        n_read = read(sock_fd, read_buffer, BUFFER_SIZE);
        read_buffer[n_read - 1] = '\0';

        if (is_debug)
        {
            printf(CLR_MAGENTA MSG_DEBUG_READ CLR_DEFAULT, read_buffer);
        }

        printf("Response: %s\n", read_buffer);
    }
}
