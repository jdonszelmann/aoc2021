with open("extra.txt") as f:
    c, f = [i.strip().split("\n") for i in f.read().split("\n\n")]

coords = []
folds = []

for i in c:
    a, b = i.split(",")
    coords.append((int(a), int(b)))

for i in f:
    a, b = i.replace("fold along", "").strip().split("=")
    folds.append((["x", "y"].index(a), int(b)))


def print_coords(coords):
    for y in range(max(i for _, i in coords) + 1):
        for x in range(max(i for i, _ in coords) + 1):
            if (x, y) in coords:
                print("█", end="")
            else:
                print(" ", end="")
        print()


def fold(axis, offset, coords):
    new = []
    for coord in coords:
        if coord[axis] < offset:
            new.append(coord)
        elif coord[axis] > offset:
            new.append(tuple(2 * offset - i if index == axis else i for index, i in enumerate(coord)))

    return new


res = fold(*folds[0], coords)

print("part 1:", len(res))

curr = coords
for i in folds:
    curr = fold(*i, curr)

print("part 2:")
print_coords(curr)

