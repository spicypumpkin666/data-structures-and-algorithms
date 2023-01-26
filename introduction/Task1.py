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

def count_things(inputs):
    numbers = []
    for record in inputs:
        if record[0] not in numbers:
            numbers.append(record[0])
        if record[1] not in numbers:
            numbers.append(record[1])
    return numbers

telephone_numbers = set(count_things(texts) + count_things(calls))

print(f"There are {len(telephone_numbers)} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
