def add_to_sorted_list(arr, value):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < value:
            low = mid + 1
        else:
            high = mid

    arr.insert(low, value)
    return arr

def choose_max(H, L):

    ph, pl = 0, 0
    maximum = 0
    for i in H:
        for j in L:
            area = (i - ph) * (j - pl)
            if maximum < area:
                maximum = area
                r0, r1 = i, j
            pl = j
        ph = i
    print(maximum)
    return r0, r1

T, n, m = map(int, input().split(" "))
H, L = [0, n], [0, m]
for i in range(T):
    inp = input().split(" ")
    if "H" in inp:
        add_to_sorted_list(H, int(inp[1]))
    else:
        add_to_sorted_list(L, int(inp[1]))

    choose_max(H, L)
