We take the input list and split it into two. Starting with the left list, we check to see if the number we're seeking
is in that list. If not we return -1 and check the right list. If the number is in the right list, we return the index
where the number exists plus the length of the left list, to find the position in the original list. If the number is in
the left list we just return the index as it is. If the number is not there we return -1.

The runtime complexity of this is O(n) where n is the number of elements in the original input list.
The space complexity is also O(n).