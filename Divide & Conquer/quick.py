import sys
sys.setrecursionlimit(10**6)

def quicksort(arr, l, r):
    if l >= r:
        return
    pivot_index = partition(arr, l, r)
    print(arr[pivot_index], end=' ')
    quicksort(arr, l, pivot_index - 1)
    quicksort(arr, pivot_index + 1, r)

def partition(arr, l, r):
    pivot = arr[l]
    i = l
    for j in range(l + 1, r + 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[i] = arr[i], arr[l]
    return i

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Run quicksort and print pivots
quicksort(arr, 0, n - 1)