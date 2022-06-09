# # # В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
# # # Пример: 1 2 3 5 8 15 23 38      Получить:   [(2, 4), (8, 64), (38, 1444)]

f = open('f.txt', 'r') # открыть файл для чтения
data = f.read() + ' '   # считать весь файл и добавить разделитель "пробел"
f.close()               # закрыть файл

numbers = []

while data != '':       # проверка на то, не пустая ли строка
    space_pos = data.index(' ')   # найти первую позиция "пробела" 
    numbers.append(int(data[:space_pos])) # взять все, что находится от начальной позиции до первого пробела и добавить список чисел
    data = data[space_pos+1:]

out = []

for e in numbers:
    if not e % 2:
        out.append((e,e **2))   # добавляем кортеж в новый список само число и квадрат этого числа
print(out)


from random import randint
from operator import length_hint 

def create_list(n):
    list = []
    for i in range(len):
        list.append(randint(1,11))
    print(list)
    return list



def sum_odd_elem(some_list):

    sum = 0
    #size = length_hint(some_list)
    for i in range(len(some_list)):
        if i%2 != 0:
            sum += some_list[i]
    return sum



len = randint(1,11)
list = create_list(len)
# print(type(list))
print(f'Список чисел: {list}')
# list = [2, 3, 5, 9, 3]

sum = sum_odd_elem(list)
print(f'Сумма эл-тов с нечетным индексом: {sum}')



# Игра с ботом (бот всегда выигрывает)

quantity = int(input("Введите количество конфет: "))
min_sweets = 1
max_sweets = int(input("Введите максимальное количество конфет за ход: "))
if quantity%(max_sweets+1) == 0:
    user_take = int(input("Сделайте свой ход: "))
    quantity = quantity - user_take
    print(f"Бот взял {quantity%(max_sweets+1)} конфет(ы).")
    quantity = quantity - (quantity%(max_sweets+1))
else:   
    print(f"Бот взял {quantity%(max_sweets+1)} конфет(ы).")
    quantity = quantity - (quantity%(max_sweets+1))

while quantity != 0:
    print(f"Оставшееся количество перед вашим ходом {quantity}")
    user_take = int(input("Сделайте свой ход: "))
    quantity = quantity - user_take
    temp = quantity%(max_sweets+1)
    quantity = quantity - (quantity%(max_sweets+1))
    print(f"Бот взял {temp} конфет(ы).")
print("Вы проиграли!!! :(")

