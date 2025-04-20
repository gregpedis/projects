#include "gatesapi.h"

struct gate_manager *g_manager;
int is_closing = 0;

void create_child(struct gate_process *gate)
{
  pid_t p = fork();
  check_neg(p, "Failed to fork");

  if (p == 0)
  {
    int i_len = snprintf(NULL, 0, "%d", gate->i);

    char *i_str = malloc(i_len + 1);
    snprintf(i_str, i_len + 1, "%d", gate->i);

    char executable[8] = "./child";
    char gate_value[2] = {gate->initial_state, '\0'};

    char *const argv[] = {executable, i_str, gate_value, NULL};
    int status = execv(executable, argv);

    /* on success, execution will never reach this line */
    check_neg(status, "Failed to create child");
  }

  printf(MAGENTA "[PARENT/PID=%d] Created child %d (PID=%d) and initial state '%c'" WHITE "\n",
         getpid(), gate->i, p, gate->initial_state);

  gate->p_id = p;
}

void on_sigusr1()
{
  for (size_t i = 0; i < g_manager->gates_count; i++)
  {
    kill(g_manager->gates[i]->p_id, SIGUSR1);
  }
}

void on_sigterm()
{
  is_closing = 1;

  for (size_t i = 0; i < g_manager->gates_count; i++)
  {
    printf(GRAY "[PARENT/PID=%d] Waiting for %d childs to exit" WHITE "\n",
           getpid(), g_manager->gates_count - i);

    kill(g_manager->gates[i]->p_id, SIGTERM);

    int status;
    pid_t pid = waitpid(g_manager->gates[i]->p_id, &status, 0);

    if (pid == -1)
    {
      perror("Sigterm on child wait went wrong.");
      exit(EXIT_FAILURE);
    }

    printf(MAGENTA GT_MESSAGE_TERMINATED WHITE "\n", getpid(), pid, status);

    free(g_manager->gates[i]);
  }

  free(g_manager->gates);
  free(g_manager);

  printf(MAGENTA GT_MESSAGE_TERMINATED_PARENT WHITE "\n", getpid());
  exit(EXIT_SUCCESS);
}

void on_sigchld()
{
  if (is_closing)
  {
    return;
  }

  for (size_t i = 0; i < g_manager->gates_count; i++)
  {
    int status;
    pid_t pid = waitpid(g_manager->gates[i]->p_id, &status, WNOHANG | WUNTRACED);

    if (pid == -1)
    {
      perror("wait for child");
      exit(EXIT_FAILURE);
    }
    else if (pid != 0)
    {

      if (WIFSTOPPED(status))
      {
        printf(MAGENTA "[PARENT/PID=%d] Child %d with PID=%d stopped. Continuing it." WHITE "\n",
               getpid(), g_manager->gates[i]->i, pid);

        kill(pid, SIGCONT);
      }
      else if (WIFEXITED(status))
      {
        printf(MAGENTA "[PARENT/PID=%d] Child %d with PID=%d exited with status code %d." WHITE "\n",
               getpid(), g_manager->gates[i]->i, pid, WEXITSTATUS(status));

        create_child(g_manager->gates[i]);
      }
      else if (WIFSIGNALED(status))
      {
        printf(MAGENTA "[PARENT/PID=%d] Child %d with PID=%d terminated by signal %d with status code %d." WHITE "\n",
               getpid(), g_manager->gates[i]->i, pid, WSTOPSIG(status), WEXITSTATUS(status));

        create_child(g_manager->gates[i]);
      }
    }
  }
}

void dispatch_signal(int signal)
{
  //printf(YELLOW "[PARENT] Got signal %d" WHITE "\n", signal);

  switch (signal)
  {
  case SIGUSR1:
    on_sigusr1();
    break;
  case SIGTERM:
    on_sigterm();
    break;
  case SIGCHLD:
    on_sigchld();
    break;
  default:
    break;
  }
}

void now_we_wait()
{
  struct sigaction action;
  action.sa_handler = dispatch_signal;
  sigaction(SIGUSR1, &action, NULL);
  sigaction(SIGTERM, &action, NULL);
  sigaction(SIGCHLD, &action, NULL);

  while (1)
    ;
}

int main(int argc, char **argv)
{
  if (argc < 2)
  {
    perror("Not enough arguments for parent process");
    exit(EXIT_FAILURE);
  }

  g_manager = gm_alloc();
  gm_init_manager(g_manager);
  gm_parse_gates_from_str(g_manager, argv[1]);

  for (size_t i = 0; i < g_manager->gates_count; i++)
  {
    create_child(g_manager->gates[i]);
  }

  now_we_wait();
  return 0;
}
