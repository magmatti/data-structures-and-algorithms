def quick_sort(array):
    arr_len = len(array)

    if arr_len <= 1:
        return array
    else:
        pivot = array.pop()

    lower_values = []
    higher_values = []

    for i in array:
        if i > pivot:
            higher_values.append(i)
        else:
            lower_values.append(i)

    return quick_sort(lower_values) + [pivot] + quick_sort(higher_values)


arr2 = [10, 1, 22, 30, -5, 100, 90]
print(arr2)

arr2 = quick_sort(arr2)
print("Sorted:")
print(arr2)