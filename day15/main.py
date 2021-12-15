import copy
import heapq

with open("input.txt") as f:
    inp = [[int(j) for j in i.strip()] for i in f.readlines()]

def add_mod(a):
    res = a + 1
    if res > 9:
        res = 1

    return res


height = len(inp)
width = len(inp[0])

def astar(x, y):
    q = []
    heapq.heappush(q, (0, (x, y, None)))

    had = set()

    while len(q) != 0:
        parent = heapq.heappop(q)
        cost, (cx, cy, cp) = parent
        if (cx, cy) in had:
            continue

        had.add((cx, cy))

        if (cx, cy) == (width - 1, height - 1):
            return cost

        for (nx, ny) in [(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)]:
            if 0 <= nx < width and 0 <= ny < height:
                risk = inp[ny][nx]
                heapq.heappush(q, (cost + risk, (nx, ny, parent)))

    return "no path"


print("part 1:", astar(0, 0))

for i in inp:
    c = copy.copy(i)
    for _ in range(4):
        c = [add_mod(a) for a in c]
        i.extend(c)

c = copy.copy(inp)
for _ in range(4):
    c = [[add_mod(x) for x in a] for a in c]
    inp.extend(c)

height = len(inp)
width = len(inp[0])

print("part 2:", astar(0, 0))