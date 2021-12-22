from functools import reduce

with open("input.txt") as f:
    inp = f.readline()

mapping = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

def find_packet_type(packet_type):
    if packet_type == 0:
        return "sum"
    elif packet_type == 1:
        return "product"
    elif packet_type == 2:
        return "minimum"
    elif packet_type == 3:
        return "maximum"
    elif packet_type == 4:
        return "literal"
    elif packet_type == 5:
        return "gt"
    elif packet_type == 6:
        return "lt"
    elif packet_type == 7:
        return "eq"
    else:
        raise ValueError(packet_type)



def parse_packet(bin_inp):
    version = int(bin_inp[0:3], 2)
    packet_type = int(bin_inp[3:6], 2)

    if packet_type == 4:
        current = 6
        res = ""
        while bin_inp[current] == "1":
            res += bin_inp[current + 1: current + 5]
            current += 5
        else:
            res += bin_inp[current + 1: current + 5]
            current += 5

        return find_packet_type(packet_type), version, res, current
    else:
        length_type_id = bin_inp[6]

        if length_type_id == "0":
            length_bin = bin_inp[7:22]
            length = int(length_bin, 2)

            pos = 0
            subpackets = []

            while pos < length:
                subdata = bin_inp[22 + pos:22 + length]
                t, v, r, c = parse_packet(subdata)
                pos += c
                subpackets.append((t, v, r, c))

            return find_packet_type(packet_type), version, subpackets, 22 + length
        else:
            length_bin = bin_inp[7:18]
            length = int(length_bin, 2)

            subpackets = []

            pos = 0
            for i in range(length):
                subdata = bin_inp[18 + pos:]
                t, v, r, c = parse_packet(subdata)

                pos += c

                subpackets.append((t, v, r, c))

            return find_packet_type(packet_type), version, subpackets, 18 + pos


def add_version(p):
    total = p[1]
    if p[0] != "literal":
        for i in p[2]:
            total += add_version(i)

    return total


def interp(p):
    if p[0] == "literal":
        return int(p[2], 2)
    else:
        values = [interp(i) for i in p[2]]

        if p[0] == "sum":
            return sum(values)
        elif p[0] == "product":
            return reduce(lambda a, v: a * v, values)
        elif p[0] == "minimum":
            return min(values)
        elif p[0] == "maximum":
            return max(values)
        elif p[0] == "gt":
            assert len(values) == 2
            return 1 if values[0] > values[1] else 0
        elif p[0] == "lt":
            assert len(values) == 2
            return 1 if values[0] < values[1] else 0
        elif p[0] == "eq":
            assert len(values) == 2
            return 1 if values[0] == values[1] else 0
        else:
            raise ValueError(p[0])


parsed = parse_packet("".join(mapping[i] for i in inp))
print("part 1:", add_version(parsed))
print("part 2:", interp(parsed))