def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = [92, 64, 74, 93, 34, 65, 78, 95, 20, 45]
print('Original:', arr)
print('Sorted:', quick_sort(arr))