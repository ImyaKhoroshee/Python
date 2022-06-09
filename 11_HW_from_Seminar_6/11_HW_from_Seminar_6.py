# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл 
# содержащий сумму многочленов.
                        
path = 'first.txt'
data = open(path, 'r')
for line in data:
    fpoly = ''
    fpoly += line       # 3*x^4+5*x^3+2*x^2+3*x^1
data.close()

path = 'second_polynominal.txt'
sp = open(path, 'r')
for line in sp:
    spoly = ''
    spoly += line       # 23*x^2+5*x^1
sp.close()

def concat_and_convert_to_list(fpoly, spoly): # функция соединяет оба многочлена и разделяет по + 
    two_poly = ''
    two_poly = fpoly + '+' + spoly
    split_poly = two_poly.split('+')
    return split_poly
    
def polynominal_to_dict(polynom):   # функция создает словарь и формирует окончателью строку (сумму многочлена)
    
    dict = {}

    for element in polynom:
        second_split_poly = element.strip().split('*') 
        if len(second_split_poly) >= 1:
            if second_split_poly[1] in dict.keys():     
                dict[second_split_poly[1]] = dict[second_split_poly[1]] + int(second_split_poly[0]) 
            else:
                dict[second_split_poly[1]] = int(second_split_poly[0])
        else:
            if 0 in dict.keys():
                dict[0] = dict[0] + int(second_split_poly[0])
            else:
                dict[0] = int(second_split_poly[0])
    
    result = ''

    for i in dict:
        if result != '':
            result += '+'
        result += str(dict[i])
        if i != 0:
            result += '*' + i
    return result

decision = polynominal_to_dict(concat_and_convert_to_list(fpoly, spoly))

dt = open('sum_of_two_polynominals', 'w')
dt.write(decision)     
dt.close()

# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

# Сжатие

data = open('smth_to_encode.txt')
for line in data:
    something_to_encode = ''
    something_to_encode += line
data.close()

def encoding_using_rle(data):
    
    data = list(data)
    count = 1
    encoded_result = '' 

    if len(data) < 2:   # если всего один символ
        return data

    for i in range(1, len(data)): 
        if data[i] != data[i-1]:      # если элемент списка не равен предыдыщему символу
            encoded_result += str(count) + data[i-1] # добавляем счетчик и, идущий перед, символ в финальный результат
            count = 1 
            data[i-1] = i 
        else:       # если элемент списка равен предыдыщему символу 
            count += 1      # плюсуем счетчик
    else: # завершение кодировки
        encoded_result += str(count) + data[i-1] 
        return encoded_result

result = encoding_using_rle(something_to_encode)
print(result)

data = open('decoding_result1.txt', 'w')
data.write(result)     
data.close()

# Восстановление

data1 = open('decoding_result1.txt')
for line in data1:
    data = ''
    data += line
data1.close()

def decoding_using_rle(data): 
    
    data = list(data)
    decoded_result = '' 
    count = '' # счетчик строкой, тк цифры записаны строкой и даже, если их переводить в число, они 
                #посчитаются неверно
    for i in range(len(data)): 
        if data[i].isdigit(): # проверка на число
            count += data[i] # записываем в счетчик
        else: # если иное чем число,
            decoded_result += data[i] * int(count) # увеличиваем элемент (символ) на то, что в счетчике, 
                                                   # предварительно переведенное в число
            count = '' # возвращаем счетчик в исходный вид
    return decoded_result

to_file = decoding_using_rle(data)
print(to_file)

data = open('decoding_result2.txt', 'w')
data.write(to_file)     
data.close()

# Кодирование списка из чисел

data = '1111111ЮЮЮЮЮ22222222223333333333'

def encoding_using_rle(data):
    
    data = list(data)
    count = 1
    encoded_result = [] 

    if len(data) < 2:   # если всего один символ
        return data

    for i in range(1, len(data)): 
        if data[i] != data[i-1]:      # если элемент списка не равен предыдущему символу
            encoded_result.append((count, data[i-1])) # добавляем счетчик и, идущий перед, символ в финальный результат
            count = 1 
            data[i-1] = i 
        else:       # если элемент списка равен предыдыщему символу 
            count += 1      # плюсуем счетчик
    else: # завершение кодировки
        encoded_result.append((count, data[i-1])) 
        return encoded_result

result = encoding_using_rle(data)
print(result)

list = [(10, '1'), (10, '2'), (10, '3')]

# Раскодирование списка из чисел

def decoding_using_rle(data): 
    
    decoded_result = '' 

    for i in range(len(data)): 
        decoded_result += data[i][0]*data[i][1]
    return decoded_result

print(decoding_using_rle(list))


# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом" 


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