class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.size = 0
        self.cache = list()
        self.cache_map = {}

    def is_empty(self):
        return self.size == 0

    def check_size(self):
        if self.size == self.capacity:
            self.remove_from_cache()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache_map.keys():
            self.check_size()
            self.cache.append(key)
            self.size += 1
            return self.cache_map[key]
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.is_empty():
            self.cache.append(key)
            self.cache_map.update({key: value})
            self.size += 1

        self.check_size()

        if key in self.cache_map.keys():
            return
        else:
            self.cache_map[key] = value
            self.cache.append(key)
            self.size += 1

    def remove_from_cache(self):
        key = self.cache.pop(0)
        self.cache_map.pop(key)
        self.size -= 1


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(f"get 1: {our_cache.get(1)}")      # returns 1
print(f"get 1: {our_cache.get(2)}")       # returns 2
print(f"get 1: {our_cache.get(9)}")      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(f"get 1: {our_cache.get(3)}") # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
cache1 = LRU_Cache(5)

cache1.set(None, None)
cache1.set(2, None)

print(f"get none: {cache1.get(None)}")      # returns None
print(f"get none, key 2: {cache1.get(2)}")      # returns None


# Test Case 2
cache2 = LRU_Cache(5)

cache2.set("string", "bla")
print(f"get string: {cache2.get('string')}")      # returns bla

cache2.set(2, 2)
cache2.set("string", 3)
cache2.set(4, 4)

print(f"get string: 3, overwritten: {cache2.get('string')}")      # returns bla


# Test Case 3
cache3 = LRU_Cache(3)

cache3.set(1, 1)
cache3.set(2, 2)
cache3.set(3, 3)
cache3.set(4, 4)


print(f"get size: {cache3.size}")      # returns 3, size of cache
print(f"get 4: {cache3.get(4)}")       # returns 4
print(f"get -1 bc we removed it from cache: {cache3.get(1)}")       # returns -1
