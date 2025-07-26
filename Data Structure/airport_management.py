# 20:40:00
def add_to_sorted_list(arr, value):
    global k
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < value:
            low = mid + 1
        else:
            high = mid

    try:
        if low < 1:
            raise IndexError
        cond1 =  value - arr[low - 1] >= k
    except IndexError:
        cond1 = True
    try:
        cond2 =  arr[low] - value >= k
    except IndexError:
        cond2 = True





    if cond1 and cond2:
        print("Permission Granted!")
        arr.insert(low, value)
    else:
        print("Permission Denied!")


n, k = map(int, input().split(" "))
srt = []
for i in range(n):
    add_to_sorted_list(srt, int(input()))


