def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

list1 = [1, 2, 6, 4, 5, 9, 4]

# Sorting using selection sort algorithm
selection_sort(list1)

print("Sorted list using selection sort:", list1)
