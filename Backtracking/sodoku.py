sudoku = [list(map(int, input().split(" "))) for _ in range(9)]
def count_zeros(sudoku):
    counter = 0
    for i in sudoku:
        for j in i:
            if j == 0:
                counter += 1
    return counter

def find_zeros(sudoku):
    lst = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                lst.append([i, j])
    return lst

total = count_zeros(sudoku)
# create_convert_table

convert_table = [[0 for _ in range(9)] for _ in range(9)]

i, j = 0, 0
new_i, new_j = 0, 0
while i < 9 and j < 9:

    if 0 <= i <= 2 and 0 <= j <= 2:
        new_i, new_j = 0, (j + 0) + (i + 0) * 3

    if 0 <= i <= 2 and 3 <= j <= 5:
        new_i, new_j = 1, (j - 3) + (i + 0) * 3

    if 0 <= i <= 2 and 6 <= j <= 8:
        new_i, new_j = 2, (j - 6) + (i + 0) * 3

    if 3 <= i <= 5 and 0 <= j <= 2:
        new_i, new_j = 3, (j + 0) + (i + -3) * 3

    if 3 <= i <= 5 and 3 <= j <= 5:
        new_i, new_j = 4, (j - 3) + (i + -3) * 3

    if 3 <= i <= 5 and 6 <= j <= 8:
        new_i, new_j = 5, (j - 6) + (i + -3) * 3

    if 6 <= i <= 8 and 0 <= j <= 2:
        new_i, new_j = 6, (j + 0) + (i + -6) * 3

    if 6 <= i <= 8 and 3 <= j <= 5:
        new_i, new_j = 7, (j - 3) + (i + -6) * 3

    if 6 <= i <= 8 and 6 <= j <= 8:
        new_i, new_j = 8, (j - 6) + (i + -6) * 3


    convert_table[i][j] = [new_i, new_j]
    j += 1
    if j == 9:
        j = 0
        i += 1

def prt(lst):
    for i in lst:
        for j in i:
            print(j, end=" ")
        print()


def convert(i, j):
    global convert_table
    new_i, new_j = convert_table[i][j]
    return new_i, new_j

squared_table = [[0 for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        val = sudoku[i][j]
        I, J = convert(i, j)
        squared_table[I][J] = val

def validate(sudoku, i, j):
    global squared_table
    value = sudoku[i][j]
    sudoku[i][j] = 0
    I, J = convert(i, j)
    squared_table[I][J] = 0
    ret_val = value not in sudoku[i] and value not in squared_table[I] and value not in [k[j] for k in sudoku]
    sudoku[i][j] = value
    squared_table[I][J] = value
    return ret_val

mini = 45
lst = find_zeros(sudoku)
def solve(sudoku, l):
    global counter, squared_table, total, mini, lst
    if l == len(lst):
        prt(sudoku)
        exit()
        return 1
    i, j = lst[l]

    for k in range(1, 10):
        sudoku[i][j] = k
        I, J = convert(i, j)
        squared_table[I][J] = k
        if validate(sudoku, i, j):
            counter = count_zeros(sudoku)

            solve(sudoku, l+1)
        sudoku[i][j] = 0
        squared_table[I][J] = 0

    return 0


solve(sudoku, 0)
print("No solution exists")