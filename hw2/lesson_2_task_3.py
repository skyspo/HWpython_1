'''Напишите функцию square, принимающую один аргумент — сторону квадрата — и возвращающую площадь квадрата.'''

import math

def square(a):
    return math.ceil(a * a)

a = float(input('введите сторону квадрата:'))
result = square(a)
input(f"Площадь квадрата со стороной {a} равна {result}")


