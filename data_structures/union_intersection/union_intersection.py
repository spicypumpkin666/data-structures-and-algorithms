"""
Your task for this problem is to fill out the union and intersection functions.
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B.
For example, the union of A = [1, 2] and B = [3, 4] is [1, 2, 3, 4].

The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both sets A and B.
For example, the intersection of A = [1, 2, 3] and B = [2, 3, 4] is [2, 3].

You will take in two linked lists and return a linked list that is composed of either the union or intersection,
respectively. Once you have completed the problem you will create your own test cases and perform your own run time
analysis on the code.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    values = list()

    node1 = llist_1.head
    node2 = llist_2.head

    while node1:
        values.append(node1.value)
        node1 = node1.next
    while node2:
        values.append(node2.value)
        node2 = node2.next
    values = sorted(set(values))

    finallist = LinkedList()

    for value in values:
        finallist.append(value)

    return finallist

def intersection(llist_1, llist_2):
    # Your Solution Here
    values1 = list()
    values2 = list()

    node1 = llist_1.head
    node2 = llist_2.head

    while node1:
        values1.append(node1.value)
        node1 = node1.next
    while node2:
        values2.append(node2.value)
        node2 = node2.next

    intersect = [i for i in values1 if i in values2]
    intersect = sorted(set(intersect))

    interlist = LinkedList()
    for i in intersect:
        interlist.append(i)

    return interlist

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2))
print(intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3,linked_list_4))
print(intersection(linked_list_3,linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [100]
element_2 = [1,0,0]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5,linked_list_6))
print(intersection(linked_list_5,linked_list_6))

# Test Case 2
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [3,2,4,35,6,65]
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7,linked_list_8))
print(intersection(linked_list_7,linked_list_8))

# Test Case 3
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = ["a", "x", "b", "z"]
element_2 = ["a", ""]

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print(union(linked_list_9,linked_list_10))
print(intersection(linked_list_9,linked_list_10))
