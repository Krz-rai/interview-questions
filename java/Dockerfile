FROM maven:3.8-openjdk-8

COPY src /usr/src/src

WORKDIR /usr/src/

RUN mvn package

CMD ["java -jar target/lru-java-0.0.1.jar"]
