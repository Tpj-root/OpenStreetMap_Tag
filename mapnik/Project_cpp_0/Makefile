# Compiler
CXX = g++
CXXFLAGS = -std=c++11 `pkg-config --cflags mapnik`
LDFLAGS = `pkg-config --libs mapnik`

# Target
TARGET = mapnik_test

# Source files
SRC = main.cpp

# Build rule
all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC) $(LDFLAGS)

# Run the program
run: $(TARGET)
	./$(TARGET)

# Clean
clean:
	rm -f $(TARGET) output.png

