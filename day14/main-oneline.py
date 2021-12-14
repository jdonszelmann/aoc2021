# print("part 1: {}\npart 2: {}".format(*(lambda reduce: (lambda template, rules: (lambda most_common, iter, occurences: (most_common(template, reduce(iter, range(10), occurences)), most_common(template, reduce(iter, range(40), occurences))))(
#     lambda template, a: (lambda a, b: a - b)(*map(lambda x: (x[1] + (template[0] == x[0]) + (template[-1] == x[0])) // 2, (lambda i: (max(i, key=lambda i: i[1]), min(i, key=lambda i: i[1])))(reduce(lambda a, v: a | {
#         v[0][0]: a.get(v[0][0], 0) + v[1],
#         v[0][1]: a.get(v[0][1], 0) + v[1] + (v[1] if v[0][0] == v[0][1] else 0)
#     }, a.items(), {}).items()))),
#     lambda acc, _: reduce(
#         lambda a, v: a | {v[0][0]: a.get(v[0][0], 0) + v[0][1], v[1][0]: a.get(v[1][0], 0) + v[1][1]},
#         (((c[0] + rules[c], n), (rules[c] + c[1], n)) for c, n in acc.items()),
#         {}
#     ),
#     reduce(lambda a, v: a | {v: a.get(v, 0) + 1}, (a + b for (a, b) in zip(template, template[1:])), {})
# ))(
#     *(lambda f: (f.readline().strip(), {i.split("->")[0].strip(): i.split("->")[1].strip() for i in f.readlines() if i.strip() != ""}))(open("input.txt"))
# ))(
#     __import__("functools").reduce
# )))

print("part 1: {}\npart 2: {}".format(*(lambda reduce: (lambda template, rules: (lambda most_common, iter, occurences: (most_common(template, reduce(iter, range(10), occurences)), most_common(template, reduce(iter, range(40), occurences))))(lambda template, a: (lambda a, b: a - b)(*map(lambda x: (x[1] + (template[0] == x[0]) + (template[-1] == x[0])) // 2, (lambda i: (max(i, key=lambda i: i[1]), min(i, key=lambda i: i[1])))(reduce(lambda a, v: a | {v[0][0]: a.get(v[0][0], 0) + v[1],v[0][1]: a.get(v[0][1], 0) + v[1] + (v[1] if v[0][0] == v[0][1] else 0)}, a.items(), {}).items()))),lambda acc, _: reduce(lambda a, v: a | {v[0][0]: a.get(v[0][0], 0) + v[0][1], v[1][0]: a.get(v[1][0], 0) + v[1][1]},(((c[0] + rules[c], n), (rules[c] + c[1], n)) for c, n in acc.items()),{}),reduce(lambda a, v: a | {v: a.get(v, 0) + 1}, (a + b for (a, b) in zip(template, template[1:])), {})))(*(lambda f: (f.readline().strip(), {i.split("->")[0].strip(): i.split("->")[1].strip() for i in f.readlines() if i.strip() != ""}))(open("input.txt"))))(__import__("functools").reduce)))




