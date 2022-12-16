"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

outgoing = set()
non_tele = set()

for text in texts:
    non_tele.add(text[0])
    non_tele.add(text[1])

for call in calls:
    outgoing.add(call[0])
    non_tele.add(call[1])

tele = outgoing.difference(non_tele)

print("These numbers could be telemarketers: ")
print(*sorted(tele), sep="\n")

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

