"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

time_on_phone = {}

for call in calls:
    if call[0] in time_on_phone.keys():
        time_on_phone[call[0]] += int(call[-1])
    if call[1] in time_on_phone.keys():
        time_on_phone[call[1]] += int(call[-1])
    if call[0] not in time_on_phone.keys():
        time_on_phone.update({call[0]: int(call[-1])})
    if call[1] not in time_on_phone.keys():
        time_on_phone.update({call[1]: int(call[-1])})

number = max(time_on_phone, key=time_on_phone.get)
seconds = time_on_phone[number]

print(f"{number} spent the longest time, {seconds} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

