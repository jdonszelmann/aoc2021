from itertools import product

with open("input.txt") as f:
    inp = f.readlines()


parsed_inp = []
for i in inp:
    if "on" in i:
        on = True
    else:
        on = False
    parts = i.replace("on", "").replace("off", "").strip().split(",")

    line = []
    for p in parts:
        a, b = p.split("=")[1].split("..")
        line.append((int(a.strip()), int(b.strip())))

    line.append(on)
    parsed_inp.append(tuple(line))

def intersection(a, b):
    for n, m in zip(a, b):
        if n[0] > m[1] or n[1] < m[0]:
            return None

    return (max(a[0][0], b[0][0]), min(a[0][1], b[0][1])), \
        (max(a[1][0], b[1][0]), min(a[1][1], b[1][1])), \
        (max(a[2][0], b[2][0]), min(a[2][1], b[2][1]))

def difference(cube1, cube2):
    int = intersection(cube1, cube2)
    if int is None:
        return [cube1]
    else:
        res = [
            (cube1[0], cube1[1], (cube1[2][0], int[2][0] - 1)),
            (cube1[0], cube1[1], (int[2][1] + 1, cube1[2][1])),
            ((cube1[0][0], int[0][0] - 1), cube1[1], int[2]),
            ((int[0][1] + 1, cube1[0][1]), cube1[1], int[2]),
            (int[0], (cube1[1][0], int[1][0] - 1), int[2]),
            (int[0], (int[1][1] + 1, cube1[1][1]), int[2])
        ]
        return [(x, y, z) for x, y, z in res if x[0] <= x[1] and y[0] <= y[1] and z[0] <= z[1]]


def volume(a):
    return abs((a[0][1] + 1 - a[0][0]) * (a[1][1] + 1 - a[1][0] ) * (a[2][1] + 1 - a[2][0]))


for part in [1, 2]:
    cur = []
    for line in parsed_inp:
        new_cur = []

        if not(
                abs(line[0][0]) <= 50 and
                abs(line[1][0]) <= 50 and
                abs(line[2][0]) <= 50 and
                abs(line[0][1]) <= 50 and
                abs(line[1][1]) <= 50 and
                abs(line[2][1]) <= 50
        ) and part == 1:
            continue

        for i in cur:
            new_cur.extend(difference(i, line[:3]))

        if line[3]:
            new_cur.append(line[:3])
        cur = new_cur

    print(f"part {part}:", sum(volume(i) for i in cur))
