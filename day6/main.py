
with open("input.txt") as f:
    inp = [int(i) for i in f.readline().split(",")]

types = [0] * 9
for i in inp:
    types[i] += 1

for i in range(256):
    zeros = types[0]
    types = types[1:] + [0]
    types[6] += zeros
    types[8] += zeros

    if i == 79:
        print("part 1:", sum(types))
print("part 2:", sum(types))


