#include "gatesapi.h"

struct gate_context *g_context;

void print_identity_message()
{
  if (g_context->state == GT_STATE_CLOSED)
  {
    printf(RED GT_MESSAGE_CLOSED WHITE "\n", g_context->i, getpid(), get_time_elapsed(g_context->timestamp));
  }
  else if (g_context->state == GT_STATE_OPEN)
  {
    printf(GREEN GT_MESSAGE_OPEN WHITE "\n", g_context->i, getpid(), get_time_elapsed(g_context->timestamp));
  }
  else
  {
    perror("This is not a valid state");
    exit(EXIT_FAILURE);
  }
}

void on_sigusr1()
{
  print_identity_message();
}

void on_sigusr2()
{
  if (g_context->state == GT_STATE_CLOSED)
  {
    g_context->state = GT_STATE_OPEN;
    print_identity_message();
  }
  else if (g_context->state == GT_STATE_OPEN)
  {
    g_context->state = GT_STATE_CLOSED;
    print_identity_message();
  }
  else
  {
    perror("Uknown current state");
    exit(EXIT_FAILURE);
  }
}

void on_sigterm()
{
  free((void *)g_context);
  exit(EXIT_SUCCESS);
}

void on_sigalrm()
{
  print_identity_message();
  alarm(ALARM_TIME);
}

void handle_signal(int signal)
{
  //printf(YELLOW "[CHILD ID=%d/PID=%d/TIME=%lds] Got Signal: %d" WHITE "\n", g_context->i, getpid(), get_time_elapsed(g_context->timestamp), signal);

  switch (signal)
  {
  case SIGUSR1:
    on_sigusr1();
    break;
  case SIGUSR2:
    on_sigusr2();
    break;
  case SIGTERM:
    on_sigterm();
    break;
  case SIGALRM:
    on_sigalrm();
    break;
  default:
    break;
  }
}

int main(int argc, char **argv)
{
  if (argc < 3)
  {
    perror("Not enough arguments for child process.");
    exit(EXIT_FAILURE);
  }

  char s = argv[2][0];
  int i;
  sscanf(argv[1], "%d", &i);

  g_context = gc_alloc();
  gc_init_context(g_context);
  gc_parse_gate_from_args(g_context, i, s);

  struct sigaction action;
  action.sa_handler = handle_signal;
  sigaction(SIGUSR1, &action, NULL);
  sigaction(SIGUSR2, &action, NULL);
  sigaction(SIGTERM, &action, NULL);
  sigaction(SIGALRM, &action, NULL);

  on_sigalrm();
  while (1)
    ;

  return EXIT_SUCCESS;
}
