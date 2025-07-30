n,m,k = map(int,input().split(" "))
matrix =[]
for i in range(n):
    matrix.append(list(map(int,input().split(" "))))

base = sum([sum(i[:k]) for i in matrix[:k]])
lst = [0 for i in range(m-1)]
for i in range(n-1):
    cb = base
    tmp = [0]
    for j in range(m-1):
        tmp.append(cb)
        if j != m-2:
            cb = cb - matrix[i][j] - matrix[i+1][j] + matrix[i+2][j] + matrix[i][j+2] + matrix[i+1][j+2]
    lst.append(tmp + [0])
    if i != n-2:
        base = base - matrix[i][0] - matrix[i][1] + matrix[i+2][0] + matrix[i+2][1]
lst.append([0 for _ in range(m-1)])


for i in range(k):
    maximum = 0
    J, K = 0, 0
    for j in range(n):
        for k in range(m):
            if maximum < lst[j][k]:
                maximum= lst[j][k]
                J, K = j, k
