def merge(left, right):
    merged = []
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(right[r])
            r += 1
        else:
            merged.append(left[l])
            l += 1
    merged += left[l:]
    merged += right[r:]

    return merged

def mergesort(items):
    if len(items) <= 1:
        return items

    med = len(items) // 2
    left = items[:med]
    right = items[med:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) < 2:
        return [-1]

    sorted_list = mergesort(input_list)

    num1 = ''
    num2 = ''

    for i in range(len(sorted_list)):
        if i % 2 == 0:
            num1 += str(sorted_list[i])
        else:
            num2 += str(sorted_list[i])
    return [int(num1), int(num2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]