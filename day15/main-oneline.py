
print("part 1: {}\npart 2: {}".format(*(lambda f, reduce, heapq: (lambda inp, push, pop, add: (lambda astar: (astar(0, 0, inp(1)), astar(0, 0, inp(5))))(
    lambda x, y, risks: reduce(lambda acc, _: acc if acc[2] != 0 else (
        lambda parent: acc if (parent[1][0], parent[1][1]) in acc[0] else (*acc[0:2], parent[0]) if (parent[1][0], parent[1][1]) == (len(risks[0]) - 1, len(risks) - 1) else (add(acc[0], (parent[1][0], parent[1][1])), reduce(lambda a, val: push(a, (parent[0] + risks[val[0]][val[1]], (val[0], val[1], parent))) if 0 <= val[0] < len(risks[0]) and 0 <= val[1] < len(risks) and (val[0], val[1]) not in acc[0] else a, [(parent[1][0] - 1, parent[1][1]), (parent[1][0] + 1, parent[1][1]), (parent[1][0], parent[1][1] - 1), (parent[1][0], parent[1][1] + 1)], acc[1]), 0)
    )(heapq.heappop(acc[1])), range(0, len(risks[0]) * len(risks) * 2), (set(),push([], (0, (x, y, None))),0))[2]
))(
    lambda n: [[(lambda a, b: a + b if a + b < 10 else a + b - 9)(int(j), x + y) for x in range(n) for j in i.strip()] for y in range(n) for i in f],
    lambda q, e: [heapq.heappush(q, e), q][1],
    lambda q: heapq.heappop(q),
    lambda s, e: [s.add(e), s][1],
))(open("input.txt").readlines(), __import__("functools").reduce, __import__("heapq"))))




print("part 1: {}\npart 2: {}".format(*(lambda f, reduce, heapq: (lambda inp, push, pop, add: (lambda astar: (astar(0, 0, inp(1)), astar(0, 0, inp(5))))(lambda x, y, risks: reduce(lambda acc, _: acc if acc[2] != 0 else (lambda parent: acc if (parent[1][0], parent[1][1]) in acc[0] else (*acc[0:2], parent[0]) if (parent[1][0], parent[1][1]) == (len(risks[0]) - 1, len(risks) - 1) else (add(acc[0], (parent[1][0], parent[1][1])), reduce(lambda a, val: push(a, (parent[0] + risks[val[0]][val[1]], (val[0], val[1], parent))) if 0 <= val[0] < len(risks[0]) and 0 <= val[1] < len(risks) and (val[0], val[1]) not in acc[0] else a, [(parent[1][0] - 1, parent[1][1]), (parent[1][0] + 1, parent[1][1]), (parent[1][0], parent[1][1] - 1), (parent[1][0], parent[1][1] + 1)], acc[1]), 0))(heapq.heappop(acc[1])), range(0, len(risks[0]) * len(risks) * 2), (set(),push([], (0, (x, y, None))),0))[2]))(lambda n: [[(lambda a, b: a + b if a + b < 10 else a + b - 9)(int(j), x + y) for x in range(n) for j in i.strip()] for y in range(n) for i in f],lambda q, e: [heapq.heappush(q, e), q][1],lambda q: heapq.heappop(q),lambda s, e: [s.add(e), s][1]))(open("input.txt").readlines(), __import__("functools").reduce, __import__("heapq"))))



