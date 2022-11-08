def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


arr = [10, 1, 22, 30, -5, 100, 90]
print(arr)

print("Sorted:")
bubble_sort(arr)
print(arr)