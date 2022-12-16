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

def get_first_text(text):
    incoming = text[0]
    answering = text[1]
    _, time = text[2].split(" ")

    print(f'First record of texts, {incoming} texts {answering} at time {time}')

def get_last_call(call):
    incoming = call[0]
    answering = call[1]
    _, time = call[2].split(" ")
    seconds = call[3]

    print(f"Last record of calls, {incoming} texts {answering} at time {time}, lasting {seconds} seconds")

get_first_text(texts[0])
get_last_call(calls[-1])

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

