# 14:24
def get_sum(ps, x0, y0, x1, y1):
    a = ps[x1][y1]
    b = ps[x0 - 1][y1]
    c = ps[x1][y0 - 1]
    d = ps[x0 - 1][y0 - 1]
    return a - b - c + d

n, m, k = map(int, input().split(" "))

lst = []
for i in range(n):
    lst.append(list(map(int, input().split(" "))))
ps = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        ps[i][j] = ps[i - 1][j] + ps[i - 1][j] - ps[i - 1][j - 1] + lst[i-1][j-1]
maximum = 0
for x0 in range(n-k):
    for y0 in range(m-k):
        for x1 in range(x0, n-k):
            for y1 in range(y0, m-k):
                area0 = get_sum(ps, x0, y0, x0+k, y0+k)
                area1 = get_sum(ps, x1, y1, x1+k, y1+k)
                total = area0 + area1
                if x0+k > x1 and y0+k > y1:
                    area2 = get_sum(ps, x1, y1, x0+k, y0+k)
                    total = total - area2
                maximum = max(maximum, total)

print(maximum)