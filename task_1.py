import random


def bubble_sort(array):
    n = 1

    while n < len(array):
        count = 0

        for i in range(len(array) - n):

            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                count += 1

        if count == 0:
            break

        n += 1
        print(array)


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
data = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(data)
bubble_sort(data)
print(data)
