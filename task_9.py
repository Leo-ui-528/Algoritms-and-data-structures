# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
def numbers(number):
    sum = 0
    for i in number:
        sum += int(i)
    return sum


number = input('Введите числа:')

max_number = 0
max_s = 0
for l in number:
    if numbers(l) > max_s:
        max_number = l
        max_s = numbers(l)

print(f' наибольшая цифра - {max_s}')
