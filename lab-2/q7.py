# WAP to sort the elements in an array using quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr = [5, 4, 9, 1, 7, 6, 10]
print("Original array:", arr)
print("Sorted array:", quick_sort(arr))