#include "common.h"
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <netinet/in.h>

#define MSG_SOCK_CREATE "[SOCKET] Creation Success\n"
#define MSG_SOCK_BIND "[SOCKET] Bind Success\n"
#define MSG_SOCK_CONNECT "[SOCKET] Connect Success\n"
#define MSG_SOCK_CLOSE "[SOCKET] Close Success\n"

#define MSG_ADDRESS_FOUND "[IP] HOST [%s] found at [%s]\n"

in_addr_t get_ip_from_hostname(char *hostname, struct UserConfig *config);

int create_socket(struct UserConfig *config)
{
    int domain = AF_INET;
    int type = SOCK_STREAM;

    int sock_fd = socket(domain, type, 0);

    if (sock_fd < 0)
    {
        perror("socket");
        exit(EXIT_FAILURE);
    }

    if (config->is_debug)
    {
        printf(CLR_GREEN MSG_SOCK_CREATE CLR_DEFAULT);
    }

    return sock_fd;
}

void bind_socket(int sock_fd, struct UserConfig *config)
{
    const struct sockaddr_in sin =
        {
            .sin_family = AF_INET,
            .sin_port = htons(0),
            .sin_addr.s_addr = htonl(INADDR_ANY),
        };

    int bind_result = bind(sock_fd, (struct sockaddr *)&sin, sizeof(sin));
    if (bind_result < 0)
    {
        perror("socket bind");
        exit(EXIT_FAILURE);
    }

    if (config->is_debug)
    {
        printf(CLR_GREEN MSG_SOCK_BIND CLR_DEFAULT);
    }
}

void connect_to_server(int sock_fd, struct UserConfig *config)
{
    const struct sockaddr_in server =
        {
            .sin_family = AF_INET,
            .sin_port = htons(config->port),
            .sin_addr.s_addr = get_ip_from_hostname(config->host, config),
        };

    int c_res = connect(sock_fd, (struct sockaddr *)&server, sizeof(server));

    if (c_res < 0)
    {
        perror("socket connect");
        exit(EXIT_FAILURE);
    }

    if (config->is_debug)
    {
        printf(CLR_GREEN MSG_SOCK_CONNECT CLR_DEFAULT);
    }
}

void close_socket(int sock_fd, struct UserConfig *config)
{
    int status = close(sock_fd);
    if (status < 0)
    {
        perror("socket close");
        exit(EXIT_FAILURE);
    }

    if (config->is_debug)
    {
        printf(CLR_GREEN MSG_SOCK_CLOSE CLR_DEFAULT);
    }
}

in_addr_t get_ip_from_hostname(char *hostname, struct UserConfig *config)
{
    struct hostent *he;
    struct in_addr addr;

    if ((he = gethostbyname(hostname)) == NULL)
    {
        perror("gethostbyname NULL error");
        exit(EXIT_FAILURE);
    }
    else
    {
        struct in_addr **addr_list;
        addr_list = (struct in_addr **)he->h_addr_list;

        if (addr_list[0] != NULL)
        {
            addr.s_addr = addr_list[0]->s_addr;
        }
        else
        {
            perror("gethostbyname EMPTY error");
            exit(EXIT_FAILURE);
        }
    }

    if (config->is_debug)
    {
        printf(CLR_YELLOW MSG_ADDRESS_FOUND CLR_DEFAULT, hostname, inet_ntoa(addr));
    }

    return addr.s_addr;
}