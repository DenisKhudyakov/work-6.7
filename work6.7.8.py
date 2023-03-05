import random

number = int(input('Загадайте число от 1 до 100 включительно: '))
start = 1
finish = 100

while True:
    N = int((finish + start) / 2)
    answer = int(input('Твоё число равно, меньше или больше, чем ' + str(N) + '?'))
    if answer == 2:
        print('Больше')
        start = N
    elif answer == 3:
        print('Меньше')
        finish = N
    elif answer == 1:
        print('Равно')
        break


