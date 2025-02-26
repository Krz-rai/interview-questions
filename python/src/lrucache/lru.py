class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.lru = {}

    def refer(self, key):
        if key in self.lru:
            self.cache.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.cache.pop()
            self.lru.pop(oldest)
            
        self.cache.insert(0, key)
        self.lru[key] = True

    def display(self):
        print(*self.cache, '')