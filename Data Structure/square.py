# 14:24
def get_sum(ps, x0, y0, x1, y1):
    a = ps[x1][y1]
    b = ps[x0][y1]
    c = ps[x1][y0]
    d = ps[x0][y0]
    return a - b - c + d


n, m, k = map(int, input().split(" "))

lst = []
for i in range(n):
    lst.append(list(map(int, input().split(" "))))
ps = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
counter = 0
for i in lst:
    for j in i:
        if j == 1:
            counter += 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + lst[i - 1][j - 1]
maximum = 0
# for x0 in range(n-k+1):
#     for y0 in range(m-k+1):
#         val = (get_sum(ps, x0, y0, x0+k-1, y0+k-1))
#         if 13 <= val <= 15:
#             print(x0, y0, val)
#         maximum = max(maximum, get_sum(ps, x0, y0, x0+k-1, y0+k-1))
for x0 in range(n - k + 1):
    for y0 in range(m - k + 1):
        for x1 in range(n - k + 1):
            for y1 in range(m - k + 1):
                # print(x0, y0, x1, y1)

                area0 = get_sum(ps, x0, y0, x0 + k, y0 + k)
                area1 = get_sum(ps, x1, y1, x1 + k, y1 + k)
                total = area0 + area1
                a, b, c, d = max(x0, x1), min(x0 + k, x1 + k), max(y0, y1), min(y0 + k, y1 + k)
                if a > b and c > d:
                    area2 = ps[b][d] - ps[a][d] - ps[b][c] + ps[a][c]
                    total = total - area2
                # print(total, maximum)
                maximum = max(maximum, total)

# print(maximum)
# print(counter)
print(n * m - counter + maximum)