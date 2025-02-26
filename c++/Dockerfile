FROM gcc:latest

COPY src /usr/src/
COPY Makefile /usr/src/

WORKDIR /usr/src/

RUN mkdir -p target && g++ -std=c++11 -o target/lru_cpp src/test.cpp

CMD ["./target/lru_cpp"]