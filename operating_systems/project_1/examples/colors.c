/**
 * \file colors.c
 * \author Aggelos Kolaitis <neoaggelos@gmail.com>
 * \date 2020-05-04
 * \brief Using ANSI escape sequences to colorize terminal output.
 */
#include <stdio.h>

#define DEFAULT "\033[30;1m"
#define RED "\033[31;1m"
#define GREEN "\033[32m"
#define YELLOW "\033[33m"
#define BLUE "\033[34m"
#define MAGENTA "\033[35m"
#define CYAN "\033[36m"
#define WHITE "\033[37m"
#define GRAY "\033[38;1m"

int main()
{
    printf(DEFAULT "Hello!" WHITE "\n");
    printf(RED "Hello!" WHITE "\n");
    printf(GREEN "Hello!" WHITE "\n");
    printf(YELLOW "Hello!" WHITE "\n");
    printf(BLUE "Hello!" WHITE "\n");
    printf(MAGENTA "Hello!" WHITE "\n");
    printf(CYAN "Hello!" WHITE "\n");
    printf(WHITE "Hello!" WHITE "\n");
    printf(GRAY "Hello!" WHITE "\n");
}
