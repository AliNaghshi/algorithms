# 25:20:82
def find(arr, value):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < value:
            low = mid + 1
        else:
            high = mid

    return low

def add(dl, lst, number):
    i = add_to_sorted_list(lst, number)
    new_dis1, new_dis2 = lst[i] - number, number - lst[i - 1]
    distance = lst[i] - lst[i-1]
    j = add_to_sorted_list(dl, distance)
    dl.pop(j)

    j = add_to_sorted_list(dl, new_dis1)
    dl.insert(j, new_dis1)
    j = add_to_sorted_list(dl, new_dis2)
    dl.insert(j, new_dis2)

    lst.insert(i, number)
    return dl[-1]






n, m, T = map(int, input().split(" "))
H, V = [0, m], [0, n]
dh, dv = [m], [n]
mh, mv = m, n
for i in range(T):
    inp = input().split(" ")
    if inp[0] == "H":
        mh = (add(dh, H, int(inp[1])))
    else:
        mv = (add(dv, V, int(inp[1])))
    print(mh * mv)