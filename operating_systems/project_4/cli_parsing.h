#include "common.h"
#include <getopt.h>

#define MSG_OPTION_FOUND "[GETOPT] Found option %s with value %s\n"
#define MSG_FLAG_FOUND "[GETOPT] Found flag %s\n"
#define MSG_CONFIG_SHOW "[CONFIG] HOST: %s PORT: %d DEBUG: %d\n"


struct UserConfig *parse_args(int argc, char *const *argv)
{
    struct UserConfig *config = alloc_default_user_config();

    int option_index = 0;
    int c;

    static struct option long_options[] =
        {
            {"DEBUG", no_argument, 0, 'd'},
            {"HOST", required_argument, 0, 'h'},
            {"PORT", required_argument, 0, 'p'},
            {0, 0, 0, 0},
        };

    while (1)
    {
        c = getopt_long_only(argc, argv, "h:p:d", long_options, &option_index);

        if (c == -1)
        {
            break;
        }

        switch (c)
        {
        case 'd':
            printf(CLR_GRAY MSG_FLAG_FOUND CLR_DEFAULT, "DEBUG");
            config->is_debug = TRUE;
            break;
        case 'h':
            printf(CLR_GRAY MSG_OPTION_FOUND CLR_DEFAULT, "HOST", optarg);
            config->host = optarg;
            break;
        case 'p':
            printf(CLR_GRAY MSG_OPTION_FOUND CLR_DEFAULT, "PORT", optarg);
            config->port = atoi(optarg);
            break;
        case '?':
        case 0:
        default:
            break;
        }
    }

    if (config->is_debug)
    {
        printf(CLR_MAGENTA MSG_CONFIG_SHOW CLR_DEFAULT, config->host, config->port, config->is_debug);
    }

    return config;
}
