
with open("input.txt") as f:
    lines = f.readlines()

formatted_lines = []
for i in lines:
    l, r = i.split(" ")
    formatted_lines.append((l, int(r)))

depth = 0
pos = 0

for (d, l) in formatted_lines:
    if d == "forward":
        pos += l
    elif d == "down":
        depth += l
    elif d == "up":
        depth -= l

print(depth, pos)
print("part 1:", depth * pos)

depth = 0
pos = 0
aim = 0

for (d, l) in formatted_lines:
    if d == "forward":
        pos += l
        depth += aim * l
    elif d == "down":
        aim += l
    elif d == "up":
        aim -= l

print(depth, pos)
print("part 2:", depth * pos)