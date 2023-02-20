We use the same trie as in problem_5 and explanation_5, except, every node contains a segment of a url instead of a single character. 
We are only looking for exact matches, not prefixes. 

Insert
Time complexity if O(n) where n is the length of the url we receieve from the router. 
Space complexity if O(n) where n is, again, the length of the url we're getting from the router. Worst case is, we need to traverse every node we have in order to insert at the proper place in the trie.

Find
Time complexity is O(n) where n is the length of the list we create using the different segments of the url (split by '/')
Space complexity is O(n) where n is the number of segments in the url we've received. 
