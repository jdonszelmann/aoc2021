with open("input.txt") as f:
    inp = [i.strip() for i in f.readlines() if i != ""]

risk = 0

basins = {}
id_ctr = 0

width = len(inp[0])
for y in range(len(inp)):
    for x in range(width):
        cur = int(inp[y][x])
        around = []
        if x > 0:
            around.append(int(inp[y][x - 1]))
        if x < width - 1:
            around.append(int(inp[y][x + 1]))
        if y > 0:
            around.append(int(inp[y - 1][x]))
        if y < len(inp) - 1:
            around.append(int(inp[y + 1][x]))

        if all(cur < i for i in around):
            basins[(x, y)] = id_ctr
            id_ctr += 1
            risk += 1 + cur

numbers = sum(len(i) for i in inp)
nines = sum(i.count("9") for i in inp)

for i in range(8):
    for y in range(len(inp)):
        for x in range(width):
            cur = int(inp[y][x])
            if cur == 9 or (x, y) in basins:
                continue

            around = []
            if x > 0:
                around.append((x - 1, y, int(inp[y][x - 1])))
            if x < width - 1:
                around.append((x + 1, y, int(inp[y][x + 1])))
            if y > 0:
                around.append((x, y - 1, int(inp[y - 1][x])))
            if y < len(inp) - 1:
                around.append((x, y + 1, int(inp[y + 1][x])))

            for (lx, ly, h) in around:
                if (lx, ly) in basins and h <= cur and h != 9:
                    basins[(x, y)] = basins[(lx, ly)]

groups = [[k for k, v in basins.items() if v == i] for i in range(id_ctr)]
groups.sort(key=len)

size = 1
for i in groups[-3:]:
    size *= len(i)

print(size)
