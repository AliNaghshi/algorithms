# 30:35:93
n = int(input())
lst = list(map(int, input().split(" ")))
queue = []
def go(ind):
    ind -= 1
    queue = [ind]
    visited = set()
    visited.add(ind)
    that_side = set()
    while queue:
        i = queue.pop(0)
        g = lst[i] - 1
        if g in that_side:
            return set()
        that_side.add(g)
        if not g in visited:
            visited.add(g)
            queue.append(g)
    return visited
sets = set()
for i in range(1, n+1):
    if (i-1) not in sets:
        sets = sets | go(i)
print(len(sets))
for i in sorted(list(sets)):
    print(i+1, end=" ")



