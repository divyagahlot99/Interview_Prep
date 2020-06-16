def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
 
arr = [4, 2, 8, 6, 4, 1, 0, 15, 4, 3]
print(bubble_sort(arr))
