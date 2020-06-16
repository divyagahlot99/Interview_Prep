def insertion_sort(arr):
    n = len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
    
arr = [4, 2, 8, 6, 4, 1, 0, 15, 4, 3]
print(insertion_sort(arr))
