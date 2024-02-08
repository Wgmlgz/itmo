CC = clang
CFLAGS = -std=c++17

# Define the target
TARGET = my_program

# Define the dependencies
DEPS = f.cpp

# Build the target
$(TARGET): $(DEPS)
	$(CC) $(CFLAGS) -o $(TARGET) $^

# Clean the project
clean:
	rm -f $(TARGET) *.o