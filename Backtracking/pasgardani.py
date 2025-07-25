n = int(input())
lst = []
inorders = 0
for i in range(n):
    lst.append(list(map(int, input().split(" ")))[1::])

def find_combinations(lst, chosen, j):
    global inorders
    if len(lst) == j:
        inorders += 1
        return

    for i in lst[j]:
        if i not in chosen:
            chosen.add(i)
            find_combinations(lst, chosen, j + 1)
            chosen.remove(i)
    return

find_combinations(lst, set(), 0)
print(inorders)

