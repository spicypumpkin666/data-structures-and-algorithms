For insert, we start at the root, and check if the sub path exists already. If yes, we continue until either it doesn't and we've reached the end or until we can insert a new sub path. 
For find, we traverse the trie the same way to check if a subpath exists, and return None if it does not, and return the handler if it does. 

Runtime is O(n) where n is the number of sub paths. 
Space is O(n) as well. 