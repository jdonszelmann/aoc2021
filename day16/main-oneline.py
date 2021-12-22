print("part 1: {}\npart 2: {}".format(*(lambda reduce, find_packet_type, mapping, inp: (lambda add_version, interp, parse_packet:(
    add_version(parse_packet("".join(mapping[i] for i in inp))),
    interp(parse_packet("".join(mapping[i] for i in inp)))
))(
    add_version := lambda p: p[1] + (0 if p[0] == "literal" else sum(add_version(i) for i in p[2])),
    interp := lambda p: int(p[2], 2) if p[0] == "literal" else (lambda values: {
        "sum": sum(values),
        "product": reduce(lambda a, v: a * v, values),
        "minimum": min(values),
        "maximum": max(values),
        "gt": (1 if values[0] > values[1] else 0) if len(values) > 1 else 0,
        "lt": (1 if values[0] < values[1] else 0) if len(values) > 1 else 0,
        "eq": (1 if values[0] == values[1] else 0) if len(values) > 1 else 0,
    })([interp(i) for i in p[2]])[p[0]],
    parse_packet := lambda bin_inp: (
        (find_packet_type(int(bin_inp[3:6], 2)), int(bin_inp[0:3], 2), *reduce(lambda acc, _: acc if acc[2] else (acc[0] + bin_inp[acc[1] + 1: acc[1] + 5],acc[1] + 5,bin_inp[acc[1]] != "1"), range((len(bin_inp) - 6) // 5), ("", 6, False))[:2])
        if int(bin_inp[3:6], 2) == 4 else (
            (find_packet_type(int(bin_inp[3:6], 2)), int(bin_inp[0:3], 2), reduce(lambda acc, _: (lambda packet: (acc[0] + [packet], acc[1] + packet[3]))(parse_packet(bin_inp[22 + acc[1]:22 + int(bin_inp[7:22], 2)])) if acc[1] < int(bin_inp[7:22], 2) else acc, range(int(bin_inp[7:22], 2)), ([], 0))[0], 22 + int(bin_inp[7:22], 2))
            if bin_inp[6] == "0"
            else (find_packet_type(int(bin_inp[3:6], 2)), int(bin_inp[0:3], 2), *(lambda a, b: (a, b + 18))(*reduce(lambda acc, _: (lambda packet: (acc[0] + [packet], acc[1] + packet[3]))(parse_packet(bin_inp[18 + acc[1]:])), range(int(bin_inp[7:18], 2)), ([], 0))))
        )
    )
))(
    __import__("functools").reduce,
    lambda packet_type: {0: "sum", 1: "product", 2: "minimum", 3: "maximum", 4: "literal", 5: "gt", 6: "lt", 7: "eq"}[packet_type],
    {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
     "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111", },
    open("input.txt").readline()
)))

# print("part 1: {}\npart 2: {}".format(*(lambda reduce, find_packet_type, mapping, inp: (lambda add_version, interp, parse_packet:(add_version(parse_packet("".join(mapping[i] for i in inp))),interp(parse_packet("".join(mapping[i] for i in inp)))))(add_version := lambda p: p[1] + (0 if p[0] == "literal" else sum(add_version(i) for i in p[2])),interp := lambda p: int(p[2], 2) if p[0] == "literal" else (lambda values: {"sum": sum(values),"product": reduce(lambda a, v: a * v, values),"minimum": min(values),"maximum": max(values),"gt": (1 if values[0] > values[1] else 0) if len(values) > 1 else 0,"lt": (1 if values[0] < values[1] else 0) if len(values) > 1 else 0,"eq": (1 if values[0] == values[1] else 0) if len(values) > 1 else 0,})([interp(i) for i in p[2]])[p[0]],parse_packet := lambda bin_inp: ((find_packet_type(int(bin_inp[3:6], 2)), int(bin_inp[0:3], 2), *reduce(lambda acc, _: acc if acc[2] else (acc[0] + bin_inp[acc[1] + 1: acc[1] + 5],acc[1] + 5,bin_inp[acc[1]] != "1"), range((len(bin_inp) - 6) // 5), ("", 6, False))[:2])if int(bin_inp[3:6], 2) == 4 else ((find_packet_type(int(bin_inp[3:6], 2)), int(bin_inp[0:3], 2), reduce(lambda acc, _: (lambda packet: (acc[0] + [packet], acc[1] + packet[3]))(parse_packet(bin_inp[22 + acc[1]:22 + int(bin_inp[7:22], 2)])) if acc[1] < int(bin_inp[7:22], 2) else acc, range(int(bin_inp[7:22], 2)), ([], 0))[0], 22 + int(bin_inp[7:22], 2)) if bin_inp[6] == "0" else (find_packet_type(int(bin_inp[3:6], 2)), int(bin_inp[0:3], 2), *(lambda a, b: (a, b + 18))(*reduce(lambda acc, _: (lambda packet: (acc[0] + [packet], acc[1] + packet[3]))(parse_packet(bin_inp[18 + acc[1]:])), range(int(bin_inp[7:18], 2)), ([], 0))))))))(__import__("functools").reuce,lambda packet_type: {0: "sum", 1: "product", 2: "minimum", 3: "maximum", 4: "literal", 5: "gt", 6: "lt", 7: "eq"}[packet_type],{"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111","8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111", },open("input.txt").readline())))
