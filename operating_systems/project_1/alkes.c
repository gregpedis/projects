#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <string.h>
#include <unistd.h>
#include <fctl.h>

#define ARGS_FILE_PATH     1
#define ARGS_PROC_COUNT_TO 2


#define FIRST_CHILD_IS_RUNNING 0
#define SECOND_CHILD_IS_RUNNING 1
#define FORK_FAILED 2

#define OUT


#define EXEC_EVEN 0
#define EXEC_ODD  1

struct args 
{
  const char* filepath;
  size_t count;
  int execution_type;
};


struct args* parse_args(int argc, char** argv)
{
  struct args* cmdLine = malloc(sizeof(struct args));
  memset(cmdLine, 0, sizeof(struct args));

  cmdLine->filepath = argv[ARGS_FILE_PATH];
  cmdLine->count = argv[ARGS_PROC_COUNT_TO];
  return cmdLine;
}

int child_execution(struct args* args)
{
  int fd = open(args->filepath, O_RDWR | O_APPEND);
  const char* message = "Message from %d\n";
  
  for(size_t i = 0; i < args->count; i++) {

    if(
        (args->execution_type == EXEC_ODD && i % 2 != 0) || 
        (args->execution_type == EXEC_EVEN && i % 2 == 0)
      ) {

      int length = snprintf( NULL, 0, "Message from %d\n", x );
      char* str = malloc( length + 1 );
      snprintf( str, length + 1, "%d", getpid());
      write(fd, (void*)str, length);
      write(fd, '\n', 1);
      free(str);
    }
  }
  exit(0);
}

void print_file(struct args* cmdLine)
{
  /* use GNU readline because we are lazy */
  FILE* fp;
  char* line = NULL;
  size_t len = 0;
  ssize_t read;
  
  fp = fopen(cmdLine->filepath, "r");
  while ((read = getline(&line, &len, fp)) != -1) {
    printf("%s", line);
  }
  fclose(fp);
  free(line);
}

void create_output_file(struct args* cmdLine)
{
  int fd2 = open(cmdLine->filepath, O_RDWR | O_CREAT, S_IRUSR | S_IRGRP | S_IROTH);
  close(fd2);
}

int main(int argc, char** argv)
{
  int res = 0;
  pid_t wait_pid;
  pid_t first_child_pid;
  pid_t second_child_pid;
  int wait_status = 0;

  struct args *cmdLine = parse_args(argc, argv);

  create_output_file(cmdLine);

  first_child_pid = fork();
  if(first_child_pid != 0 && first_child_pid != -1) {

      cmdLine->execution_type = EXEC_EVEN;
      child_execution(cmdLine);

      second_child_pid = fork();
      if(second_child_pid != 0 && second_child_pid != -1) {

        cmdLine->execution_type = EXEC_ODD;
        child_execution(cmdLine);
      }
    }

  }

  while((wait_pid = wait(&status)) > 0);

  print_file(cmdLine);

  return res;
}
