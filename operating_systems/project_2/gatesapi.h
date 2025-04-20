#ifndef GATESAPI_H_
#define GATESAPI_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <time.h>

#define DEFAULT "\033[30;1m"
#define RED "\033[31;1m"
#define GREEN "\033[32m"
#define YELLOW "\033[33m"
#define BLUE "\033[34m"
#define MAGENTA "\033[35m"
#define CYAN "\033[36m"
#define WHITE "\033[37m"
#define GRAY "\033[38;1m"

#define GT_STATE_CLOSED 'f'
#define GT_STATE_OPEN 't'

#define GT_MESSAGE_OPEN "[ID=%d/PID=%d/TIME=%lds] The gates are open!"
#define GT_MESSAGE_CLOSED "[ID=%d/PID=%d/TIME=%lds] The gates are closed!"

#define GT_MESSAGE_TERMINATED "[PARENT/PID=%d] Child with PID=%d terminated successfully with exit status code %d!"
#define GT_MESSAGE_TERMINATED_PARENT "[PARENT/PID=%d] All children exited, terminating as well"

#define WAIT_TIME 2
#define ALARM_TIME 15

struct gate_process
{
  int i;
  pid_t p_id;
  char initial_state;
};

struct gate_context
{
  int i;
  char state;
  time_t timestamp;
};

struct gate_manager
{
  size_t gates_count;
  struct gate_process **gates;
};

void check_neg(int ret, const char *msg)
{
  if (ret < 0)
  {
    perror(msg);
    exit(EXIT_FAILURE);
  }
}

time_t get_time_elapsed(time_t since)
{
  return time(NULL) - since;
}

struct gate_context *gc_alloc()
{
  return (struct gate_context *)malloc(sizeof(struct gate_context));
}

void gc_init_context(struct gate_context *context)
{
  memset(context, 0, sizeof(struct gate_context));
}

void gc_parse_gate_from_args(
    struct gate_context *context, int i, char state)
{
  context->i = i;
  context->state = state;
  context->timestamp = time(NULL);
}

struct gate_manager *gm_alloc()
{
  return (struct gate_manager *)malloc(sizeof(struct gate_manager));
}

void gm_init_manager(struct gate_manager *manager)
{
  memset(manager, 0, sizeof(struct gate_manager));
}

void gm_init_gate(struct gate_process *gate, int id, pid_t process, char state)
{
  gate->i = id;
  gate->p_id = process;
  gate->initial_state = state;
}

void gm_parse_gates_from_str(struct gate_manager *manager, const char *gates_string)
{
  size_t length = strlen(gates_string);
  manager->gates = (struct gate_process **)malloc(sizeof(struct gate_process *) * length);
  manager->gates_count = length;
  for (size_t i = 0; i < length; i++)
  {
    manager->gates[i] = (struct gate_process *)malloc(sizeof(struct gate_process));
    gm_init_gate(manager->gates[i], i, -1, gates_string[i]);
  }
}

#endif
