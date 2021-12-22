with open("input.txt") as f:
    algo_unparsed, rest = f.read().split("\n\n")

trench_map = [[1 if j == "#" else 0 for j in i] for i in rest.split("\n") if i != ""]
algo = [1 if i == "#" else 0 for i in algo_unparsed if i != ""]


def enhance_3x3(m, x, y, d):
    w, h = len(m[0]), len(m)

    bits = []
    for y_l in range(y - 1, y + 2):
        for x_l in range(x - 1, x + 2):
            if 0 <= y_l < h and 0 <= x_l < w:
                bits.append("1" if m[y_l][x_l] else "0")
            else:
                bits.append("1" if d else "0")

    assert len(bits) == 9
    number = int("".join(bits), 2)
    return algo[number]


def enhance(m, d):
    w, h = len(m[0]), len(m)

    res = []
    for y in range(-1, h + 1):
        line = []
        for x in range(-1, w + 1):
            line.append(enhance_3x3(m, x, y, d))

        res.append(line)

    return res, enhance_3x3(m, -10, -10, d)


def print_trench_map(m):
    w, h = len(m[0]), len(m)
    for y in range(h):
        for x in range(w):
            print("#" if m[y][x] else ".", end="")
        print()


def reenhance(n, m):
    d = 0
    for i in range(n):
        m, d = enhance(m, d)

    return sum(sum(i) for i in m)


print("part 1:", reenhance(2, trench_map))
print("part 2:", reenhance(50, trench_map))