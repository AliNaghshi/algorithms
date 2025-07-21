input()
lst = list(map(int, input().split(" ")))

n = len(lst) - 1
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            dp[i][j] = 0

for i in range(2, n+1):
    for j in range(n-i+1):
        end = i + j - 1
        for k in range(j, end):
            cost = dp[j][k] + dp[k+1][end] + lst[j]*lst[k+1]*lst[end+1]
            dp[j][end] = cost if dp[j][end] > cost or dp[j][end] == 0 else dp[j][end]



print(dp[0][n-1])
