/**
 * \file args.c
 * \author Aggelos Kolaitis <neoaggelos@gmail.com>
 * \date 2020-03-02
 * \short Example program that parses command line arguments
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STREQUAL(x, y) (strncmp((x), (y), strlen(y)) == 0)

/**
 * \short Print program usage and exit
 */
void usage(const char *prog)
{
    printf("Usage: %s [--fruit [APPLE/ORANGE/MELLON]]\n", prog);
    exit(EXIT_FAILURE);
}

/**
 * Program entry point.
 */
int main(int argc, char **argv)
{
    const char *chosen_fruit = NULL;

    // Print all arguments
    for (int i = 1; i < argc; i++)
    {
        printf("Argument %d: '%s'\n", i, argv[i]);
    }

    // Parse command-line arguments
    for (int i = 1; i < argc; i++)
    {
        if (STREQUAL(argv[i], "--fruit"))
        {
            if (i == argc - 1)
            {
                // --fruit was passed as the last argument, error
                usage(argv[0]);
            }
            else
            {
                // argv[i] == "--fruit", so argv[i+1] has the choice
                int is_valid_choice = STREQUAL(argv[i + 1], "APPLE") || STREQUAL(argv[i + 1], "ORANGE") || STREQUAL(argv[i + 1], "MELLON");

                if (is_valid_choice)
                {
                    chosen_fruit = argv[i + 1];
                }
                else
                {
                    usage(argv[0]);
                }
            }
        }
    }

    printf("Your choice was: %s\n", chosen_fruit ? chosen_fruit : "(none)");
    return 0;
}
