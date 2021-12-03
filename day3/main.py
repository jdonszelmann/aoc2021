import copy

with open("input.txt") as f:
    inp = f.readlines()

inp = [i.strip() for i in inp]


def common(lst, position, most=True):
    ones = sum((int(i[position]) for i in lst))
    zeroes = sum((1 - int(i[position]) for i in lst))

    if most:
        return "1" if ones >= zeroes else "0"
    else:
        return "1" if zeroes > ones else "0"


most_common_one = ""
most_common_zero = ""

for i in range(len(inp[0])):
    most_common_one += common(inp, i, True)
    most_common_zero += common(inp, i, False)

print("part 1:", int(most_common_one, 2) * int(most_common_zero, 2))


def ox_or_fuel(lst, ox=True):
    lst_copy = copy.copy(lst)

    for i in range(len(lst_copy[0])):
        most_common = common(lst_copy, i, ox)
        lst_copy = [j for j in lst_copy if j[i] == most_common]

        if len(lst_copy) == 1:
            return lst_copy[0]

    assert False


print("part 2:", int(ox_or_fuel(inp, True), 2) * int(ox_or_fuel(inp, False), 2))


