# 5:32:43
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

n = int(input())
srt = []
for i in range(n):
    m = int(input())
    add_to_sorted_list(srt, m)
    print(srt[(i) // 2])