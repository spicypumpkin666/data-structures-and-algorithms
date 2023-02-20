In this problem we construct a Trie to build an autocomplete function. 

We first create a TrieNode class that will be the nodes of our trie. This holds the node's children, and a binary (true / false) of if the word has been completed or not.
We also create a class that will hold the trie itself, with an initializing root node, and insert and find functions.
For insert, with each word we check if the character already exists in our dict. If yes, we move on to the next character. If no, the character is added. 
For find, we walk through the tree based on the characters we're looking for. For instance, if we're given 'f' as a prefix and our trie contains 'fun' and 'free', 
we will get a list back like ['fun', 'free']. If we submit 'fr' as a prefix in this example our find function narrows down the choices further and will
only return ['free'].

Insert
Time complexity is O(n) where n is len(word) we're inserting
Space complexity is O(n) where n is the number of nodes we have in the trie- we need to theoretically traverse every node in the tree to make sure the char we're trying to store either already exists or 
is inserted in the proper place. 

Find
Time complexity is O(n) where n is the length of the prefix we're given. 
Space complexity doesn't matter as we aren't storing anything. 

Find_words ('suffixes' function)
Time complexity is O(n) where n is the number of nodes, as we need to theoretically visit every node to build our set of suffixes to return. 
Space complexity is O(n) where n is again the number of nodes in our trie, the worst case is that every single node in our trie needs to be returned as a match. 
