# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример: 6 -> да     7 -> да     1 -> нет

def check_if_weekend(arg):
    match arg:
        case 1:
            print('Today is Monday, working day!')
        case 2:
            print('Today is Tuesday, working day!')
        case 3:
            print('Today is Wednesday, working day!')
        case 4:
            print('Today is Thursday, working day!')
        case 5:
            print('Today is Friday, working day!')
        case 6:
            print('Congratulations, today is Saturday - weekend!')
        case 7:
            print('Congratulations, today is Sunday - weekend!')

number = int(input('Enter one digit designating the day of week: '))
if number > 7:
    print('Sorry, there is no such day of week!')
check_if_weekend(number)


# Задача 2. Напишите программу, которая принимает на вход координаты точки (X и Y), и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:     x=34; y=-30 -> 4    x=2; y=4-> 1    x=-34; y=-30 -> 3

def get_quart(x, y):
    if x > 0 and y > 0:
        return 1   
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0: 
        return 4
    else:           # Это если пользователь введет нули. 
        return 0    # Можно сюда было сразу вывести 57 строку, но я не знала как правильнее с точки зрения языка python.
                    # Вот вопрос вам :) Правильнее везде return оставить или можно print в else написать, а после вызова функции тогда проверку на нули убрать?
x_coordinate = int(input('Enter coordinate for x: '))
y_coordinate = int(input('Enter coordinate for y: '))

quart_num = get_quart(x_coordinate, y_coordinate)
if quart_num == 0:
    print('It is impossible to identify a quarter clearly.')
else: 
    print(f'This point is located in the quarter number {quart_num}.')


# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных 
# координат точек в этой четверти (x и y).

def range_of_coordinates_by_quarter():
    
    quarter = int(input('Enter the number of the quarter: '))
    
    if quarter == 1:
        print('Coordinates of points: x > 0 and y > 0')  
    elif quarter == 2:
        print('Coordinates of points: x < 0 and y > 0')  
    elif quarter == 3:
        print('Coordinates of points: x < 0 and y < 0')  
    elif quarter == 4:
        print('Coordinates of points: x > 0 and y < 0')  
    else:   # Это если пользователь введет число, отличное от номеров четвертей. 
        print('This quarter does not exist.') 

range_of_coordinates_by_quarter()


# Задача 4. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример: A (3,6); B (2,1) -> 5,09        A (7,-5); B (1,-1) -> 7,21

def get_distance(x1, y1, x2, y2):
    xDistance = x2 - x1
    yDistance = y2 - y1
    return round(((xDistance**2) + (yDistance**2))**(0.5), 2)
   
xA = int(input('Enter X of point A: ')) 
yA = int(input('Enter Y of point A: '))
xB = int(input('Enter X of point B: '))  
yB = int(input('Enter Y of point B: '))
distance = get_distance(xA, yA, xB, yB)
print(distance)
