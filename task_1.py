#Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#Python 3.8.8 64 bit (AMD64)] on win32
import random
import sys

# Урок 3, задание 1.
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

array = [random.randint(2, 99) for _ in range(97)]
for n in range(2, 10):

    array[n] = []
    for f in range(2, 100):
        if f % n == 0:
            array[n].append(f)
    #print(f'Для числа {n} кратны - {len(array[n])}')

sum_size = 0
sum_size += sys.getsizeof(array)
sum_size += sys.getsizeof(f)
sum_size += sys.getsizeof(n)
print(f'Сумма использованной памяти в программе №1: {sum_size}')

result = {}
for m in range(2, 10):
    result[m] = []
    for d in range(2, 100):
        if d % m == 0:
            result[m].append(d)
    #print(f'Для числа {m} кратны - {len(result[m])}. Кратные числа: {result[m]}')

sum_size = 0
sum_size += sys.getsizeof(result)
sum_size += sys.getsizeof(d)
sum_size += sys.getsizeof(m)
print(f'Сумма использованной памяти в программе №2: {sum_size}')


a = [0]*8
for i in range(2,100):
    for j in range(2,10):
        if i%j == 0:
            a[j-2] += 1
i = 0
while i < len(a):
    #print(i+2, ' - ', a[i])
    i += 1

sum_size = 0
sum_size += sys.getsizeof(range)
sum_size += sys.getsizeof(j)
sum_size += sys.getsizeof(a)
print(f'Сумма использованной памяти в программе №3: {sum_size}')


#Вывод
#Список элементов dict наиболее эффективно использует память в программе №2