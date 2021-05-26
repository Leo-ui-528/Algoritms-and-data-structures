# 5 В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
import timeit
import cProfile

array = [random.randint(-5000, 5000) for _ in range(10000)]


def mbz_while(size):
    # array = [random.randint(-5000, 5000) for _ in range(10000)]

    num = 100
    i = 0
    index = -1
    while i < num:
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1
        return f'Максимальное отрицательное число {array[index]} ' \
               f'находится в ячейке {index}'


print(timeit.timeit('mbz_while(10)', number=1000, globals=globals()))  # 0.0007025209999999976
print(timeit.timeit('mbz_while(100)', number=1000, globals=globals()))  # 0.0006772319999999998
print(timeit.timeit('mbz_while(1000)', number=10000, globals=globals()))  # 0.007326282999999996


def mbz_for(size):
    num = float('-inf')
    for i, item in enumerate(array):
        if 0 > item > num:
            num = item
            index = i

    if num != float('-inf'):
        return f'Максимальное отрицательное число {num} находится в ячейке {index}'


print(timeit.timeit('mbz_for(10)', number=1000, globals=globals()))  # 0.775486312
print(timeit.timeit('mbz_for(100)', number=1000, globals=globals()))  # 0.7644719959999999
print(timeit.timeit('mbz_for(1000)', number=10000, globals=globals()))  # 8.104066241000002


def mbz_c_in_c(size):
    num = 100000
    i = 0
    index = -1
    while i < num:
        if i < 0 and index == -1:
            index = i
        elif 0 > i > index:
            index = i
            for i in array:
                if i == -5:
                    print("-5")
                    for i in array:
                        if i == -10:
                            print("-10")

        i += 1
    return f'Максимальное отрицательное число {num} находится в ячейке {index}'


print(timeit.timeit('mbz_c_in_c(10)', number=1000, globals=globals()))  # 10.755704322
print(timeit.timeit('mbz_c_in_c(100)', number=1000, globals=globals()))  # 11.106373730999998
print(timeit.timeit('mbz_c_in_c(1000)', number=10000, globals=globals()))  # 107.79055612100001

cProfile.run('mbz_c_in_c(1000000000000000000000000000000000)')

# 4 function calls in 0.013 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.013    0.013 <string>:1(<module>)
#         1    0.013    0.013    0.013    0.013 task_1.py:47(mbz_c_in_c)
#         1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вывод:
# Взадаче 1 с использванием цикла while прослеживается линейная асимптотика.
# В задаче 2 используется цикл for in видна линейная асимптотика.
# В задаче 3 с вложенными циклами тоже линейная асимптотика.
#Функцию стоит оптимизировать.
