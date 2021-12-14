from collections import defaultdict
from functools import reduce

with open("input.txt") as f:
    template = f.readline()
    rules = {i.split("->")[0].strip(): i.split("->")[1].strip() for i in f.readlines() if i.strip() != ""}

sequence = list(template.strip())

occurences = defaultdict(int)

for i in range(len(sequence) - 1):
    a = sequence[i]
    b = sequence[i + 1]
    occurences[a + b] += 1


def iter(acc, _):
    new = defaultdict(int)

    for (c, n) in acc.items():
        res = rules[c]

        new[c[0] + res] += n
        new[res + c[1]] += n

    return new


def most_common(a):
    counter = defaultdict(int)
    for c, i in a.items():
        counter[c[0]] += i
        counter[c[1]] += i

    ranking = sorted(counter.items())
    _most_common_char, _most_common = max(ranking, key=lambda i: i[1])
    _least_common_char, _least_common = min(ranking, key=lambda i: i[1])

    if _most_common_char == sequence[0]:
        _most_common += 1

    if _least_common_char == sequence[0]:
        _least_common += 1

    if _most_common_char == sequence[-1]:
        _most_common += 1

    if _least_common_char == sequence[-1]:
        _least_common += 1

    return _most_common // 2 - _least_common // 2


print("part 1:", most_common(reduce(iter, range(10), occurences)))
print("part 2:", most_common(reduce(iter, range(40), occurences)))

