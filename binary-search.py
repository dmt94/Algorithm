def binary_search(target, arr):
    low = 0
    n = len(arr)
    high = len(arr) - 1
    while low <= high:
        median = int((low + high) / 2)
        if arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return low != n and arr[low] == target
