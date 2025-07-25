n, k = map(int, input().split(" "))
sets = set()
def go(i, j, remain):
    global n, sets

    if remain == 0:
        sets.add((i, j))
        return

    directions = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

    for dx, dy in directions:
        x, y = i + dx, j + dy
        if 0 <= x < n and 0 <= y < n:
            go(x, y, remain-1)
            x += dx
            y += dy
go(0, 0, k)
print(len(sets))