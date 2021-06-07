import random


def merge_sort(array):
    if len(array) <= 1:
        return array
    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:len(array)])

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        array[k] = right[j]
        j = j + 1
        k = k + 1
    return array


SIZE = 10
LIMIT = 50
data = [random.uniform(0, LIMIT) for i in range(SIZE)]
print(data)
merge_sort(data)
print(data)



