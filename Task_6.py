from itertools import count

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

from itertools import cycle

my_list = [False, 'Python', 888, None]
с = 0
for el in cycle(my_list):
    if с > 8:
        break
    print(el)
    с += 1
