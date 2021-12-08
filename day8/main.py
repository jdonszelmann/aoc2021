
with open("input.txt") as f:
    inp = [i.split("|") for i in f.readlines()]

inps = []
outs = []

for (i, o) in inp:
    inps.append(i.strip().split(" "))
    outs.append(o.strip().split(" "))


c = 0

for i in outs:
    for num in i:
        if len(num) in [2, 4, 3, 7]:
            c += 1
print(c)

c = 0
for i, o in zip(inps, outs):
    patterns = {}
    for num in i:
        if len(num) == 2:
            patterns[1] = num
        elif len(num) == 3:
            patterns[7] = num
        elif len(num) == 4:
            patterns[4] = num
        elif len(num) == 7:
            patterns[8] = num

    for num in i:
        if all(x in num for x in patterns[1]) and num not in patterns.values():
            if len(num) == 5:
                patterns[3] = num
            else:
                if all(x in num for x in patterns[4]):
                    patterns[9] = num
                else:
                    patterns[0] = num
        elif num not in patterns.values():
            if all(x in num for x in patterns[4] if x not in patterns[1]) and len(num) == 5:
                patterns[5] = num
            else:
                if len(num) == 5:
                    patterns[2] = num
                else:
                    patterns[6] = num

    res = []
    for i in o:
        for k, v in patterns.items():
            if all(x in i for x in v) and len(v) == len(i):
                res.append(k)
                break

    x = int("".join(str(i) for i in res))
    c += x

print(c)


