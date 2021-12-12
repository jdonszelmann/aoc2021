import copy
from collections import defaultdict
from functools import lru_cache

with open("input.txt") as f:
    inp = f.readlines()


neighbors = defaultdict(list)
for i in inp:
    a, b = i.strip().split("-")
    neighbors[a].append(b)
    neighbors[b].append(a)


def search(cur, had, chain, part, print_paths):
    had = copy.deepcopy(had)

    if any(i > 1 for i in had.values()) or part == 1:
        if cur in had:
            return 0

    if cur == "start" and cur in had:
        if print_paths:
            print(chain)
        return 0


    if cur == "end":
        return 1

    if cur.islower():
        had[cur] += 1

    neighbours = neighbors[cur]
    total = 0
    for i in neighbours:
        total += search(i, had, chain + [cur] if print_paths else [], part, print_paths)

    return total



print("part 1:", search("start", defaultdict(int), [], 1, False))
print("part 2:", search("start", defaultdict(int), [], 2, False))

