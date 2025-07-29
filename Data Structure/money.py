q = int(input())
dic = {}
for i in range(q):
    for j in list(map(int, input().split(" ")))[1:]:
        if i+j not in dic:
            dic[i+j] = [j]
        else:
            dic[i+j].append(j)
    for j in range(i, int("+inf")):
        if k=



