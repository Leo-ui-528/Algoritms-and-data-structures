# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра,
# которую необходимо посчитать,
# задаются вводом с клавиатуры.
number = input('Введите цифру для поиска: ')
x = 0
y = 0
while x <= 5:
    numbers = input('Введите последовательность: ')
    for i in numbers:
        if number == i:
            y += 1
    x += 1

print(f'Цифра {number} встречается в последовательности : {y} раз(a)')
