print("part 1: {}\npart 2: {}".format(*(lambda r, s: (s(80,r), s(256,r)))(__import__("functools").reduce, lambda n, reduce: sum(reduce(lambda i, _: [*i[1:7], i[7] + i[0], i[8], i[0]], range(n), (lambda n: list(map(lambda i: n.count(i), range(0, 9))))([int(i) for i in open("input.txt").readline().split(",")]))))))

