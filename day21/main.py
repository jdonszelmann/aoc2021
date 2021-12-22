import itertools
from collections import defaultdict, Counter

p1 = 4
p2 = 5

# p1 = 4
# p2 = 8

die_value = 1
rolls = 0
def roll():
    global die_value, rolls
    v = die_value
    die_value += 1

    if die_value > 100:
        die_value = 1

    rolls += 1

    return v


p1_score = 0
p2_score = 0

other_score = 0

while True:
    p1_roll = sum(roll() for _ in range(3))

    p1 += p1_roll
    while p1 > 10:
        p1 -= 10

    p1_score += p1
    if p1_score >= 1000:
        other_score = p2_score
        break

    p2_roll = sum(roll() for _ in range(3))

    p2 += p2_roll
    while p2 > 10:
        p2 -= 10

    p2_score += p2
    if p2_score >= 1000:
        other_score = p1_score
        break

print("part 1:", rolls * other_score)

# p1 = 4
# p2 = 5

p1 = 4
p2 = 8

positions = defaultdict(int)
positions[(p1, p2, 0, 0, 0)] = 1

wins = [0, 0]

while len(positions):
    new_positions = defaultdict(int)
    for (*rest, cur), amount in positions.items():
        for a, b, c in itertools.product(range(1, 4), repeat=3):
            new_pos = (rest[0] + a + b + c - 1) % 10 + 1
            new_score = rest[2] + new_pos
            if new_score >= 21:
               wins[cur] += amount
            else:
                new_positions[(rest[1], new_pos, rest[3], new_score, 1 - cur)] += amount

    positions = new_positions

print("part 2:", max(wins))
