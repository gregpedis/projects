TARGETS = factorial_pipes 

# Phony targets. 
.PHONY: all clean

# Targets to build when running `make`
all: $(TARGETS)

# Run `make clean` to delete binaries and object files.
clean:
	rm -rf $(TARGETS) *.o

# Targets to build `factorial_pipes` binary
factorial_pipes: factorial_pipes.o
	gcc factorial_pipes.o -o factorial_pipes 
factorial_pipes.o: factorial_pipes.c
	gcc factorial_pipes.c -c -o factorial_pipes.o

