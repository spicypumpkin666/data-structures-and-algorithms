import hashlib
import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Chain:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, data):
        timestamp = datetime.datetime.now()

        if self.head is None:
            self.head = Block(timestamp=timestamp, data=data, previous_hash=None)
            self.last = self.head
        else:
            block = self.last
            self.last = Block(timestamp=timestamp, data=data, previous_hash=None)
            self.last.previous_hash = block

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
chain = Chain()
testtime = datetime.datetime.now()
chain.append(2)
chain.append("potato")

print(f"should be potato: {chain.last.data}")
# Test Case 2
print(f"should be {testtime}: {chain.last.timestamp}")
# Test Case 3
print(f"should be 2: {chain.head.data}")
