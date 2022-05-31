# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101      3 -> 11         2 -> 10

# Вариант 1

import math

def transform_of_decimal_to_binary(number):
    binary_num = ''
    while(number >= 1):
        binary_num = str(math.floor(number%2))+binary_num
        number=number/2
    return binary_num

decimal = (int(input('Enter your decimal number: ')))
print(transform_of_decimal_to_binary(decimal))

# Вариант 2

print(bin(decimal))


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonacci(n):
    
    list1 = []
    fib1 = 0
    fib2 = 1
    list1.append(fib1)
    list1.append(fib2)

    for i in range(2, n+1):
        fib1, fib2 = fib2, fib1 + fib2 
        list1.append(fib2)

    list2 = []
    fib3 = 0
    fib4 = 1
    list2.insert(0, fib4)

    for i in range(2, n+1):
        elem = fib3 - fib4
        fib3, fib4 = fib4, elem 
        list2.insert(0, elem)
 
    list2.extend(list1) 
    print (str(list2))
    return list2

number = int(input('Enter your number: '))
Fibonacci(number)

# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве 
# символа-разделителя используйте пробел.

def find_max_and_min(string):
    string = string.split(" ")
    print(string)

    print(max(string))
    print(min(string))

str = '2 0 7 6 5 4'
find_max_and_min(str)

# Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

from math import gcd
 
def lcm(a, b):
    return a * b // gcd(a, b)
 
a = 5
b = 7
print(lcm(a, b))
