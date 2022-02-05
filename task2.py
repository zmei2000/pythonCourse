length_square = int(input('Введите длину стороны квадрата: '))
perimeter_square = length_square * 4
area_square = length_square * length_square
print('Вывод:')
print('Периметр:', str(perimeter_square))

length_rectangle = int(input('Введите длину прямоугольника: '))
width_rectangle = int(input('Введите ширину прямоугольника: '))
perimeter_rectangle = (length_rectangle + width_rectangle) * 2
area_rectangle = length_rectangle * width_rectangle
print('Вывод: \nПериметр:', str(perimeter_rectangle))
print('Площадь:', str(area_rectangle))
