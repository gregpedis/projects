#include "cli_parsing.h"
#include "socket_ops.h"
#include "commands.h"

int main(int argc, char *const *argv)
{
    printf(CLR_DEFAULT);
    // cli parsing operations.
    struct UserConfig *config = parse_args(argc, argv);
    // socket operations.
    int sock_fd = create_socket(config);
    bind_socket(sock_fd, config);
    connect_to_server(sock_fd, config);
    // command operations.
    execute_command_loop(sock_fd, config->is_debug);
    return 0;
}
