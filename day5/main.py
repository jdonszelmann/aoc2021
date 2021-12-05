from collections import defaultdict
from functools import reduce
from itertools import groupby

coords = []
with open("test.txt") as f:
    for i in f.readlines():
        l, r = i.split("->")

        x1, y1 = map(int, l.split(","))
        x2, y2 = map(int, r.split(","))
        coords.append((x1, y1, x2, y2))



sign = lambda x: x and (1, -1)[x<0]


def calculate(lst, f=lambda *args: True):

    res = defaultdict(int)
    for (x1, y1, x2, y2) in lst:
        if f(x1, y1, x2, y2):
            print((x1, y1, x2, y2))
            dx = sign(x2 - x1)
            dy = sign(y2 - y1)

            for x in ((x1 + dx * i, y1 + dy * i) for i in range(1 + max(abs(x2 - x1), abs(y2 - y1)))):
                res[x] += 1


    print(res)
    c = 0
    for i in res.values():
        if i > 1:
            c += 1

    return c


print("part 1:", calculate(coords, lambda x1, y1, x2, y2 : x1 == x2 or y1 == y2))
print("part 2:", calculate(coords))
