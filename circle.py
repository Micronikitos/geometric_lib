import math


def area(r):
""" Название функции: area 
Описание: Вычисляет площадь круга с заданным радиусом. 
Пример вызова: area_value = area(5) 
@param r Радиус круга. 
@return Возвращает площадь круга. """
    return math.pi * r * r


def perimeter(r):
""" Название функции: perimeter
Описание: Вычисляет периметр (длину окружности) круга с заданным радиусом.
Пример вызова: perimeter_value = perimeter(5) 
@param r Радиус круга. 
@return Возвращает периметр круга. """
    return 2 * math.pi * r

