

print("part 1: {}\npart 2: {}".format(*(lambda r, c, m, y:(lambda p:(int("".join([m(y, i, True) for i in range(len(y[0]))]), 2) * int("".join([m(y, i, False) for i in range(len(y[0]))]), 2), int(p(c.copy(y), True)[1], 2) * int(p(c.copy(y), False)[1], 2)))(lambda l, o: r(lambda a, v: (lambda x: (x, x[0] if len(x) == 1 else None))([j for j in a[0] if j[v] == m(a[0], v, o)]) if a[1] is None else a, (i for i in range(len(l[0]))), (l, None))))(__import__("functools").reduce, __import__("copy"), lambda l, p, m: (lambda z, o: ("1" if o >= z else "0") if m else ("1" if z > o else "0"))(sum((1 - int(i[p]) for i in l)), sum((int(i[p]) for i in l))), [i.strip() for i in open("input.txt").readlines()])))


