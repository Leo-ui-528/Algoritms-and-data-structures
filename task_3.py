# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
number_1 = int(input('Введите число: '))
number_2 = 0
while number_1 > 0:
    last_n = number_1 % 10
    number_1 = number_1 // 10
    number_2 = number_2 * 10
    number_2 = number_2 + last_n

print(f'{number_2} - Обратное число')
