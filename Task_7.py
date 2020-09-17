from itertools import count
from math import factorial


def gen():
    for n in count(1):
        yield factorial(n)


x = 0
for i in gen():
    if x < 15:
        print(i)
        x += 1
    else:
        break
