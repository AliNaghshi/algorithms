import copy


def prt(lst):
    for i in lst:
        for j in i:
            print(j, end=' ')
        print()


def place(board, l, row):
    global k, total

    if l == k:
        total += 1
        return

    for i in range(row, len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                cpy = copy.deepcopy(board)
                find_threats(board, i, j)
                place(board, l + 1, i+1)
                board = cpy


def find_threats(board, i, j):
    n = len(board)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (-1, -1), (1, -1)]

    board[i][j] = 2
    for dx, dy in directions:
        x, y = i + dx, j + dy
        while 0 <= x < n and 0 <= y < n:
            board[x][y] = 1
            x += dx
            y += dy


answers = [[0 for i in range(8)] for _ in range(8)]
for i in range(8):
    for j in range(8):
        n, k = i+1, j+1
        board = [[0 for _ in range(n)] for _ in range(n)]
        total = 0
        place(board, 0, 0)
        answers[i][j] = total
        print(i, j)
print(answers)