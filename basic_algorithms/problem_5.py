class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        if char not in node.children:
            node.children[char] = TrieNode()

    def find_words(self, suffix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        suffixes = []

        if self.is_word:
            suffixes += [suffix]

        for (char, node) in self.children.items():
            suffixes += node.find_words(suffix + char)

        return suffixes


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return node

    def match(self, prefix):
        node = self.find(prefix)
        if node:
            return node.find_words(prefix)
        return []


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.find_words()))
        else:
            print(prefix + " not found")
    else:
        print('')

print(f('')); #should return nothing
print(f('ant')); #should return ["ant", "anthology", "antagonist", "antonym",]
print(f('f')); #should return ["fun", "function", "factory", ]
print(f('trig')); #should return ["trigger", "trigonometry",]
