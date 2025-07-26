# 35:34:06

def add_to_sorted_list(arr, value):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid][0] < value[0]:
            low = mid + 1
        else:
            high = mid

    arr.insert(low, value)
    return arr

n = int(input())
subs = []
for i in range(n):
    inp = input().split(" ")[1:]
    for j in range(len(inp) // 2):
        name = inp[j * 2]
        number = int(inp[j * 2 + 1])
        add_to_sorted_list(subs, [name, number])
    removes = []
    for j in subs:
        if j[1] <= 1:
            removes.append(j)
        else:
            j[1] -= 1
    for j in removes:
        subs.remove(j)
    if subs:
        removes.append(subs[0])
        subs.pop(0)
    for j in sorted(removes, key=lambda x: x[0]):
        print(j[0], end=" ")


    print()


