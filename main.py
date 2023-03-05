# Задание №1
while True:
    number = int(input('Введите число: '))
    number **= 3
    print(number)
    if number == 0:
        break
print('')
# Задание №2
name = input('Введите имя должника: ')
credit = int(input('Введите размер долга: '))
print(name, 'Ваща задолженность составляет', credit)
while credit > 0:
    payment = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
    credit -= payment
    if credit <= 0:
        print('Отлично', name + '! Вы погасили долг. Спасибо!')
        break
    print('Маловато,', name, 'Давайте ещё раз.')
print('')
# Задание №3
while True:
    number1 = int(input('Введите число: '))
    print('Количество цифр равно:', len(str(number1)))
    break
print('')
# Задание №4
negative = 0
positive = 0
while True:
    mark = int(input('Введите число '))
    if mark > 0:
        positive += 1
    elif mark < 0:
        negative += 1
    else:
        break
print('Кол-во положительных чисел:', positive)
print('Кол-во отрицательных чисел:', negative)
print('')
# Задание №5
work_day = 1
call_wife = False
sum_task = 0
index_wife = 0
while work_day <= 8:
    task = int(input('Сколько задач решит Максим? '))
    call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    index_wife += call
    call_wife = (index_wife != 0)
    sum_task += task
    work_day += 1
print('Рабочий день закончился. Всего выполнено задач:', sum_task)
if call_wife:
    print('Нужно зайти в магазин.')


