
# input
x0, x1 = 209, 238
y0, y1 = -86, -59

# test
# x0, x1 = 20, 30
# y0, y1 = -10, -5


def simulate(dx, dy):
    x, y = 0, 0

    highest_y = 0

    while True:
        x += dx
        y += dy

        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        dy -= 1

        if y > highest_y:
            highest_y = y

        if x >= x0 and x <= x1 and y >= y0 and y <= y1:
            return highest_y

        if (x > x1 and y > y1) or (dx == 0 and (x >= x1 or x < x0)) or (dx == 0 and y < y1):
            return None


max_y = float("-inf")
bx = 0
by = 0

for y in range(-100, 100):
    for x in range(-100, 100):
        res = simulate(x, y)
        if res != None:
            if res > max_y:
                max_y = res
                bx = x
                by = y

print("part 1:", bx, by, max_y)

count = 0
for y in range(-500, 500):
    if y % 100 == 0:
        print(y)
    for x in range(-500, 500):
        res = simulate(x, y)
        if res != None:
            count += 1

print("part 2:", count)