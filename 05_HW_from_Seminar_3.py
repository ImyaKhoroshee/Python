# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов 
# списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_of_odd_elements(list):
   
    for i in list:
        odd_elem_sum = sum(list[1::2])
        print(odd_elem_sum)
        return odd_elem_sum
        
my_list = [2, 3, 5, 9, 3]
sum_of_odd_elements(my_list)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д. Если остается 1 элемент без пары - 
# умножаем его самого на себя.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];  [2, 3, 5, 6] => [12, 15]

def product_of_pair_of_numbers(list):
    
    list2 = []
    if len(list) % 2 == 0:
        for i in range(len(list)//2):
            result = list[i]*list[-i-1]
            list2.append(result)
            print(list2)
    if len(list) % 2 != 0:   
        for i in range(len(list)//2):
            result = list[i]*list[-i-1]
            list2.append(result)
        add = len(list)//2
        add2 = list[add]*list[add]
        list2.append(add2)
        print(list2)
    
    return list2

my_list = [2, 3, 5, 6, 2]
product_of_pair_of_numbers(my_list)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:[1.1, 1.2, 3.1, 5, 10.01] => 0.19

def difference(list):
    max = 0
    min = 100 
    for i in range(len(list)):
        result = round(list[i] - int(list[i]), 2)
        if result > max:
            max = result   
        if result < min:
            min = result
    print(f'Maximum: {max}')
    print(f'Minimum: {min}')
    final_result = round((max-min), 2)
    print(f'Difference: {final_result}')

float_list = [1.25, 1.02, 3.15, 5.05, 10.10]
difference(float_list)