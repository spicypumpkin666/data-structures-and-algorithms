def sqrt(number):
    count = 0
    target = 1

    while number > 0:
        number = number - target
        target += 2
        count += 1

    if number < 0:
        return count - 1

    return count

print("Pass" if  (3 == sqrt(9)) else "Fail")
print("Pass" if  (0 == sqrt(0)) else "Fail")
print("Pass" if  (4 == sqrt(16)) else "Fail")
print("Pass" if  (1 == sqrt(1)) else "Fail")
print("Pass" if  (5 == sqrt(27)) else "Fail")
