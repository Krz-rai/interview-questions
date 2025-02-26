Results for the Software Interview Problems
===

# Problem - 1

- C++ Docker Image

```
Fixed the Docker image by:
1. Using the gcc:latest image
2. Creating the target directory before compilation
3. Using g++ instead of gcc for proper C++ standard library linking
4. Fixed the path to the executable in the CMD
```

-  Python Docker Image

```
Fixed the Python Docker image by:
1. No structural issues with the original Dockerfile
2. Implemented the missing LRUCache.refer() method in lru.py
```

- Java Docker Image

```
Fixed the Java Docker image by:
1. Adding missing HashSet import
2. Setting the correct Java version (1.8) in pom.xml
3. Fixing the CMD command to use separate arguments
4. Adding proper mainClass configuration in maven-jar-plugin
```

# Problem - 2

- C++ Build

```
Fixed the C++ build by:
1. Creating target directory before compilation
2. Using clang++ instead of clang for proper standard library linking
3. Using the -std=c++14 flag to specify C++ standard
4. Command: mkdir -p target && clang++ -std=c++14 -o target/lru_cpp src/test.cpp
```

- Java Build

```
Fixed the Java build by:
1. Adding missing jdk.version property in pom.xml
2. Adding the HashSet import in LRUCache.java
3. Implementing the missing refer() method functionality
4. Adding proper mainClass configuration for the JAR
```

- Python Run

```
Fixed the Python implementation by:
1. Implementing the LRUCache.refer() method to:
   - Check if the key is in the cache
   - Remove the least recently used item if the cache is full
   - Update the cache order placing most recently used items at the front
```

# Problem - 3

- C++ Docker Run Output

```
5 4 3 1
```

- Java Docker Run Output

```
5 4 3 1
```

- Python Docker Run Output

```
5 4 3 1
```