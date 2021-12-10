
with open("input.txt") as f:
    inp = [i.strip() for i in f.readlines() if i.strip() != ""]

correct_costs = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

closing = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

opening_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

def corrupted(line):
    s = []
    for i in line:
        if i in closing:
            opening = closing[i]
            actual = s.pop()
            if opening != actual:
                return correct_costs[i], []
        else:
            s.append(i)

    return 0, [opening_map[i] for i in s[::-1]]


res = sum(corrupted(i)[0] for i in inp)
print(res)

autocomplete_costs = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

discarded_input = [c[1] for i in inp if (c := corrupted(i))[0] == 0]

totals = []
for i in discarded_input:
    total = 0
    for c in i:
        total = total * 5 + autocomplete_costs[c]

    totals.append(total)

totals.sort()
print(totals[len(totals) // 2])
