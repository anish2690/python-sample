from math import sqrt
import math
a = [1, 2, 45, 5]

print(len(a))  # length of list


print(sqrt(4))

print(math.pi)

# func with annotations


def func_2(a: int, b: int):  # just for doc
    return a * b
 

print(func_2('a', 20))
print(func_2(10, 20))
print(func_2([1, 3], 2))
