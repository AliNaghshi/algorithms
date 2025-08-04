n, q = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))

savor = []
for i in range(n):
    I, J = 0, i
    for j in range(n):# optimize this part
        if j < i:
            if lst[j] < lst[i]:
                I = j + 1
        else:
            if lst[j] >= lst[i]:
                J = j
            if lst[j] < lst[i]:
                break
    savor.append([I, J])

for i in range(q):
    a, b = map(int, input().split(' '))
    for j in range(n):
        if savor[j][0] <= a <= j <= b <= savor[j][1]:
            print(lst[j])
            break
