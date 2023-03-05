# Задание №6
X = int(input('Положите ваши сбережения: '))
P = float(input('Под какой процент? '))
Y = int(input('Сумма по окончанию вклада: '))
year = 0
while X <= Y:
    year += 1
    X += int(X * (P / 100))
print('Срок сбережения:', year)
print('')

# Задание №7
import random

number1 = int(random.uniform(0, 20.0))
attempt = 0
while True:
    answer = int(input('Угадайте число от 0 до 20: '))
    attempt += 1
    if answer < number1:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    elif answer > number1:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Красавчик! Количество попыток:', attempt)
        break

