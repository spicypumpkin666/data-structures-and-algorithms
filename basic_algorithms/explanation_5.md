For insert, with each word we check if the character already exists in our dict. If yes, we move on to the next character. If no, the character is added. 
For find, we walk through the tree based on the characters we're looking for. 

Runtime for a find is O(n), where n is the number of letters in the word

Space complexity is O(x * n) where n is, again, the number of letters in the word and x is the number of words