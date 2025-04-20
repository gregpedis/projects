TARGETS = ask4
flags= -Wall -Wextra -Wpedantic -g -O1

# Phony targets. 
.PHONY: all clean remake

# Targets to build when running `make`
all: $(TARGETS)

# Run `make clean` to delete binaries and object files.
clean:
	rm -rf $(TARGETS) *.o

# Run `make remake` to combine `clean` and `all` phony targets.
remake:
	make clean && make all

# Targets to build `ask4` binary
ask4: ask4.o
	gcc ask4.o -o ask4
ask4.o: ask4.c
	gcc ask4.c -c -o ask4.o



