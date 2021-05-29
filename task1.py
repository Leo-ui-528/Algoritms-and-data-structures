#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.
from collections import deque, defaultdict

while True:
    try:
        number = int(input('Введите количество компаний: '))
    except ValueError:
        print('Вы ввели недопустимое значение')
        continue
    break

companies = defaultdict(int)
prof_c = deque()
unprofit_c = deque()
all_profit = 0
QUARTER = 4

for i in range(number):
    name = input(f'Введите название {i+1}й компании: ')
    profit = 0
    q = 1
    while q <= QUARTER:
        try:
            profit += int(input(f'Введите прибыль за {q}й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение')
            continue
        q += 1
    companies[name] = profit
    all_profit += profit

middle_profit = all_profit / number
for i, item in companies.items():
    if item >= middle_profit:
        prof_c.append(i)
    else:
        unprofit_c.append(i)
print(f'Средняя прибыль: {middle_profit}')
print(f'Прибыль выше среднего у компании:')
for name in prof_c:
    print(name)
print(f'Прибыль ниже среднего у компании:')
for name in unprofit_c:
    print(name)
