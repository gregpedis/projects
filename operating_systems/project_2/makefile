TARGETS = child parent
flags= -Wall -Wextra -Wpedantic -g -O1

# Targets to build when running `make`
all: $(TARGETS)


# Phony targets. Executed always.
.PHONY: all clean

# Targets to build `child` binary
child: child.o
	gcc child.o $(flags) -o child
child.o: child.c
	gcc child.c -c $(flags) -o child.o

# Targets to build `parent` binary
parent: parent.o
	gcc parent.o $(flags) -o parent
parent.o: parent.c
	gcc parent.c $(flags) -c -o parent.o

# Targets to build in one-step
child-onestep: child.c
	gcc child.c -o child
parent-onestep: parent.c
	gcc parent.c -o parent 

# Run `make clean` to delete binaries and object files.
clean:
	rm -rf $(TARGETS) *.o

