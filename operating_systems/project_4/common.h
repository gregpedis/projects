#ifndef FILE_COMMON_SEEN // once-only header.
#define FILE_COMMON_SEEN

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>

#define CLR_DEFAULT "\033[30;1m"
#define CLR_RED "\033[31;1m"
#define CLR_GREEN "\033[32m"
#define CLR_YELLOW "\033[33m"
#define CLR_BLUE "\033[34m"
#define CLR_MAGENTA "\033[35m"
#define CLR_CYAN "\033[36m"
#define CLR_WHITE "\033[37m"
#define CLR_GRAY "\033[38;1m"

#define TRUE 1
#define FALSE 0

#define DEFAULT_HOST "lab4-server.dslab.os.grnetcloud.net"
#define DEFAULT_PORT 18080
#define DEFAULT_DEBUG FALSE

struct UserConfig
{
    char *host;
    int port;
    int is_debug;
};

struct UserConfig *alloc_default_user_config()
{
    struct UserConfig *config = (struct UserConfig *)malloc(sizeof(struct UserConfig));
    config->host = DEFAULT_HOST;
    config->port = DEFAULT_PORT;
    config->is_debug = DEFAULT_DEBUG;
    return config;
}

#endif /* !FILE_COMMON_SEEN */