TARGET=$(CURDIR)/target

dummy:=$(shell mkdir -p $(TARGET))

.DEFAULT: all

.PHONY: all clean

all: src/test.cpp
	$(CXX) $(CXXFLAGS) -std=c++14 -stdlib=libc++ -o $(TARGET)/lru_cpp src/test.cpp

clean:
	-rm -rf target