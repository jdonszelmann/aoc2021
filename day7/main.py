
with open("input.txt") as f:
    inp = [int(i) for i in f.readline().split(",")]



print("part 1:", min({p: sum(abs(i - p) for i in inp) for p in range(0, max(inp) * 2)}.items(), key=lambda i: i[1])[1])
print("part 2:", min({p: sum((abs(i - p) * (abs(i - p) - 1)) // 2 for i in inp) for p in range(0, max(inp) * 2)}.items(), key=lambda i: i[1])[1])