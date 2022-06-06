# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = randint(2,10)
lst = [randint(0, 101) for i in range(k+1)] # list comprehension для коэфф.
res_list = [str(x) for x in lst]    # перевод списка коэфф. в строку для дальшейшей работы

def polynomial(arg_list, k): # функция для многочлена степени k
    res = ''
    n = k
    for i in arg_list:
        if k > 0:
            res = res + i + "*x^" + str(k) + "+"
            k = k - 1
        else:
            res = res + i  
    print(f'k = {n} => {res} = 0')  # больше для меня :)
    res = 'k = ' + str(n) + ' => ' + res + ' = 0'
    return res  # возврат результата

to_file = polynomial(res_list, k)   # запись результата в переменную для дальшейшей записи в файл
data = open('file.txt', 'w')
data.write(to_file)     
data.close()

# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает 
# одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

path = '09_numbers.txt'
data = open(path, 'r')  # считывание файла
for line in data:
    numbers = ''
    numbers += line     # Запись в строковую переменную для дальнейшей сортировки
data.close()

numbers = [int (x) for x in numbers.split()]    # избавление от пробелов
print(f'Original numbers = {numbers}')
sorted_numbers = sorted(numbers)    # сортировка по возрастанию
print(f'Sorted numbers = {sorted_numbers}')

def miss_number(list):      # функция для проверки по заданному условию
    res = ''
    for i in range(len(list)):
        if i > 0: 
            if not list[i] - 1 == list[i-1]:
                res = list[i]-1     # запись результата в переменную для дальнейшей работы. в случае необходимости
    return res

miss_number(sorted_numbers)
print(f'Missed number: {miss_number(sorted_numbers)}') 

# Дана последовательность чисел. Получить список уникальных элементов заданной 
# последовательности. Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

from random import randint

def list_form(n):
    
    data = [randint(1, 10) for i in range(n)]
    print(data)     # для наглядности
    return data

def unique_list(list):
    
    uniq_list = [i for i in list if list.count(i) < 2]  # Если количество раз, когда элемент встречается, меньше 2,
    return uniq_list                                    # то добавляем в новый список

number = randint(5,10)
print(unique_list(list_form(number)))