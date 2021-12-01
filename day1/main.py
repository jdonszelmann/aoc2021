
with open("input.txt") as f:
    inp_lines = f.readlines()

inp = [int(i) for i in inp_lines if i != ""]


def increasing(lst):
    last = lst[0]
    count = 0
    for i in lst[1:]:
        if i > last:
            count += 1
        last = i
    return count


print(f"part 1: {increasing(inp)}")

windows = [sum(inp[i:i + 3]) for i in range(len(inp))]

print(f"part 2: {increasing(windows)}")
