
print("part 1: {}\npart 2:\n{}".format(*(lambda c, z, p, f, r: (lambda coords, folds: (
    len(set(f(*folds[0], coords))), p(r(lambda a, v: f(*v, a), folds, coords))
))(
    [tuple(map(int, i.split(","))) for i in c],
    [(lambda a, b: (["x", "y"].index(a), int(b)))(*i.replace("fold along", "").strip().split("=")) for i in z]
))(
    *[i.strip().split("\n") for i in open("input.txt").read().split("\n\n")],
    lambda p: "\n".join("".join("█" if (x, y) in p else " " for x in range(max(i for i, _ in p) + 1)) for y in range(max(i for _, i in p) + 1)),
    lambda a, o, c: [x if x[a] < o else tuple(2 * o - i if p == a else i for p, i in enumerate(x)) for x in c if x[a] != o],
    __import__("functools").reduce
)))

print("part 1: {}\npart 2:\n{}".format(*(lambda c, z, p, f, r: (lambda coords, folds: (len(f(*folds[0], coords)), p(r(lambda a, v: f(*v, a), folds, coords))))([tuple(map(int, i.split(","))) for i in c],[(lambda a, b: (["x", "y"].index(a), int(b)))(*i.replace("fold along", "").strip().split("=")) for i in z]))(*[i.strip().split("\n") for i in open("input.txt").read().split("\n\n")],lambda p: "\n".join("".join("█" if (x, y) in p else " " for x in range(max(i for i, _ in p) + 1)) for y in range(max(i for _, i in p) + 1)),lambda a, o, c: [x if x[a] < o else tuple(2 * o - i if p == a else i for p, i in enumerate(x)) for x in c if x[a] != o],__import__("functools").reduce)))








