To find the square root of a number we can count how many times we subtract the target (an incrementing
number starting at 1) from the number (which we decrease each time by the value of the target until we reach 0).

The runtime complexity here is O(n), where n is the value of the square root (ie. the number of times we need to
subtract something from the number to reach 0).
The space complexity is O(1).