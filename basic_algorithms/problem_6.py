
import random

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    _min = ints[0]
    _max = ints[1]

    for i in ints:
        if i < _min:
            _min = i
        if i > _max:
            _max = i

    return _min, _max

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

z = [75, 45, 25, 15, 65, 85, 55, 15, 45, 95]
random.shuffle(z)

print ("Pass" if ((15, 95) == get_min_max(z)) else "Fail")

x = [0,0,0,0,0,0,0,0,0,0]
print ("Pass" if ((0, 0) == get_min_max(x)) else "Fail")
