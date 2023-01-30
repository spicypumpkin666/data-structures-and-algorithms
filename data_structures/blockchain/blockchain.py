import hashlib
import datetime


class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "We are going to encode this string of data!".encode('utf-8')
        sha.update(hash_str)
        sha.update(str(self.timestamp).encode('utf-8'))
        sha.update(str(self.data).encode('utf-8'))
        sha.update(str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

    def print_block(self):
        print(f"block timestamp {self.timestamp}")
        print(f"block data {self.data}")
        print(f"block prev hash {self.previous_hash}")
        print(f"block hash {self.hash}")



class Node:

    def __init__(self, index, block, prev_hash):
        self.index = index
        self.block = block
        self.previous = prev_hash


class Blockchain:

    def __init__(self):
        self.index = 0
        self.first_block = Block("first block", None)
        self.head = Node(self.index, self.first_block, None)

    def add_block(self, data):
        self.index += 1

        node = self.head
        new_block = Block(data=data, previous_hash=node.block.hash)
        new_node = Node(self.index, new_block, self.head)
        self.head = new_node

    def print_chain(self):
        node = self.head
        while node is not None:
            print(node.block.print_block())
            node = node.previous

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: happy route
chain = Blockchain()
chain.add_block(2)
chain.add_block("potato")
print("*******")
print("Test 1")
print(f"print chain: {chain.print_chain()}")
print(f"should be potato: {chain.head.block.data}")

# Test Case 2: add none value doesn't affect block building
chain2 = Blockchain()
chain2.add_block(1)
chain2.add_block(None)
chain2.add_block(2)
print("*******")
print("Test 2")
print(f"print chain: {chain.print_chain()}")
print(f"should print None: {chain2.head.previous.block.data}")

# Test Case 3: should add 100 blocks & print last 5
print("*******")
print("Test 3")
print(f"print chain: {chain.print_chain()}")
chain3 = Blockchain()
for i in range(100):
    chain3.add_block(i)

curr = chain3.head
for _ in range(5):
    print(f"index {curr.index}")
    curr = curr.previous

