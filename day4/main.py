
boards = []
with open("input.txt") as f:
    line1 = f.readline()
    numbers = [int(i) for i in line1.split(",")]
    f.readline()

    while True:
        board = []
        for i in range(5):
            line = f.readline()
            board.append([int(i) for i in line.split()])
        boards.append(board)
        rest = f.readline()
        if rest == "":
            break



def check_board(b):
    for i in range(len(b)):
        num_complete = 0
        for j in range(len(b[0])):
            if b[j][i] == None:
                num_complete += 1
        if num_complete == 5:
            return True

    for j in range(len(b[0])):
        num_complete = 0
        for i in range(len(b[0])):
            if b[j][i] == None:
                num_complete += 1
        if num_complete == 5:
            return True

    return False


def remove_number(i, b):
    for x in b:
        for index, j in enumerate(x):
            if j == i:
                x[index] = None


def score(i, b):
    return i * sum([sum((y for y in x if y is not None)) for x in b])


won = []
for i in numbers:
    new_boards = []
    for b in boards:
        remove_number(i, b)
        if check_board(b):
            if len(won) == 0:
                print("part 1:", score(i, b))

            won.append((b, i))
        else:
            new_boards.append(b)
    boards = new_boards

print("part 2:", score(won[-1][1], won[-1][0]))



