
print("part 1: {}\npart 2: {}".format(*(
    lambda f, y, Counter: (y(f, "start", Counter(), 1), y(f, "start", Counter(), 2)))
    (
        *(lambda reduce, defaultdict, copy: (lambda mapping: (
            lambda self, cur, had, part: (
                cur == "end" if ((any(i > 1 for i in had.values()) or part == 1 or cur == "start") and cur in had) or cur == "end" else
                [had.update([cur]) if cur.islower() else None, sum(self(self, i, copy.deepcopy(had), part) for i in mapping[cur])][1]
            ),
            lambda i, *args: i(i, *args),
            __import__("collections").Counter
        ))(
            reduce(lambda a, v: [a[v[0]].append(v[1]), a[v[1]].append(v[0]), a][2], [i.strip().split("-") for i in open("input.txt").readlines()], defaultdict(list))
        )
    )(__import__("functools").reduce, __import__("collections").defaultdict, __import__("copy")))
))
