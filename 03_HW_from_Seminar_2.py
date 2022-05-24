# Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр(отсекаем минус, считаем все в плюс).
# Пример: 67,82 -> 23       0,56 -> 11

def sum_of_digits(arg):
    
    arg = abs(arg)      # отсечение минуса
    arg = str(arg)      # преобразование в строку
    
    sum = 0
    for digit in arg:
        if digit.isdigit():       # проверка на число
            sum += int(digit)   # извлечение числа из строки и преобразование к целочисленному типу int:
    
    print(sum)
    return sum

sum_of_digits(float(input('Enter your decimal number: ')))

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

def like_factorial(N):
    
    result = 1

    for i in range(N+1):
        print(i, end=" ")
        
    print()
    
    for j in range(1, N+1):
        result = result * j
        print(result, end = ' ')
    
like_factorial(int(input('Enter your digit: ')))

# Реализуйте случайное перемешивания списка.
# *Пример:* Исходный вариант -> ['Веселый пианист', 250, 3.14, 'True '] 
# Результат -> [250, 3.14, 'True ', 'Веселый пианист']

import random

def list_mixing(arg):
    
    random.shuffle(list)    # функция для случайного перемешивания списка
    print(arg) 
    return arg

list = ['Веселый пианист', 250, 3.14, 'True ']
print(list)
list_mixing(list)

