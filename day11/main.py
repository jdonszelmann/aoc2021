import copy

with open("input.txt") as f:
    inp = [[int(j) for j in i if j.isnumeric()] for i in f.readlines()]


def check(lst, flashed, x, y):
    if y < 0 or y >= len(lst) or x < 0 or x >= len(lst[0]):
        return

    lst[y][x] += 1

    if lst[y][x] > 9 and not flashed[y][x]:
        flashed[y][x] = True

        check(lst, flashed, x, y + 1)
        check(lst, flashed, x - 1, y + 1)
        check(lst, flashed, x + 1, y + 1)
        check(lst, flashed, x, y - 1)
        check(lst, flashed, x - 1, y - 1)
        check(lst, flashed, x + 1, y - 1)
        check(lst, flashed, x + 1, y)
        check(lst, flashed, x - 1, y)


def step(lst):
    flashed = [[False] * len(lst[0]) for i in range(len(lst))]
    flashes = 0

    for y in range(len(lst)):
        for x in range(len(lst[y])):
            check(lst, flashed, x, y)

    for y in range(len(lst)):
        for x in range(len(lst[y])):
            if lst[y][x] > 9:
                flashes += 1
                lst[y][x] = 0

    return flashes


part1 = copy.deepcopy(inp)
flashes = 0
for i in range(100):
    flashes += step(part1)


print("part 1:", flashes)

part2 = copy.deepcopy(inp)
i = 1
while True:
    step(part2)

    if sum(sum(p) for p in part2) == 0:
        print("part 2:", i)
        break
    i += 1

