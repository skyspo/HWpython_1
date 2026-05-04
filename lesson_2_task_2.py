"""Создайте функцию is_year_leap, принимающую 1 аргумент — год (число) — и возвращающую 
True, если год високосный, иalse
 — если иначе.
Год високосный, если его номер делится на 4 без остатка. Например, 2020 или 2008. 2009 или 2023 не делится на 4 без остатка, значит, год не високосный.
"""
def is_year_leap(year):
    return 'true' if year % 4 == 0 else 'false'

year = int(input('vvod goda:'))
result = is_year_leap(year)
print(f"год {year}:{result}")

