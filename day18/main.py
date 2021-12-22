from math import ceil, floor

with open("input.txt") as f:
    inp = [eval(i.replace("[", "(").replace("]", ")")) for i in f.readlines()]


def add_to_first_l(a, b):
    if type(a) == int:
        return a + b
    else:
        return (add_to_first_l(a[0], b), a[1])


def add_to_first_r(a, b):
    if type(a) == int:
        return a + b
    else:
        return (a[0], add_to_first_r(a[1], b))


def print_tree(a, depth=0):
    if type(a) == int:
        print("\t" * depth, a)
    elif type(a[0]) == int and type(a[1]) == int:
        print("\t" * depth, a)
    else:
        print("\t" * depth, "(")
        print_tree(a[0], depth + 1)
        print_tree(a[1], depth + 1)
        print("\t" * depth, ")")


def reduce(a, tp, depth=0):
    if type(a) == int:
        if a >= 10 and tp == "split":
            # print("split ", a, end=" ")
            return (floor(a / 2), ceil(a / 2)), [], 1
        else:
            return a, [], 0
    elif depth == 4 and tp == "explode":
        # explode
        # print("explode ", a, end=" ")
        return 0, [("l", a[0]), ("r", a[1])], 1
    else:
        assignments = []

        res1, assignments1, modified1 = reduce(a[0], tp, depth + 1)
        if modified1 > 0:
            res2, assignments2, modified2 = a[1], [], 0
        else:
            res2, assignments2, modified2 = reduce(a[1], tp, depth + 1)

        for (direction, number) in assignments1:
            if direction == "l":
                assignments.append((direction, number))
            else:
                res2 = add_to_first_l(res2, number)

        for (direction, number) in assignments2:
            if direction == "r":
                assignments.append((direction, number))
            else:
                res1 = add_to_first_r(res1, number)

        return (
                   res1,
                   res2
               ), assignments, modified1 + modified2


def add(a, b):
    res = (a, b)
    # print(res)
    modified = 1
    while modified > 0:
        while modified > 0:
            res, _, modified = reduce(res, "explode")
            # print("reduced to ")
            # print(res)

        res, _, modified = reduce(res, "split")

    return res


def magnitude(a):
    if type(a) == int:
        return a
    else:
        return magnitude(a[0]) * 3 + magnitude(a[1]) * 2


total = inp[0]
for i in inp[1:]:
    # print(total, "+", i, "=")
    total = add(total, i)
    # print()

# print(total)
print("part 1:", magnitude(total))


print("part 2:", max(max(magnitude(add(i, j)), magnitude(add(j, i))) for i in inp for j in inp if i != j))

# [[[[6, 7], [6, 7]], [[7, 7], [0, 7]]], [[[8, 7], [7, 7]], [[8, 8], [8, 0]]]]
# [[[[5, 6], [7, 9]], [[7, 8], [7, 6]]], [[[0, 7], [7, 7]], [[8, 8], [8, 0]]]]
