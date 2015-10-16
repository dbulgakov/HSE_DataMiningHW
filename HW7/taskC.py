# -*- coding: utf-8 -*
# Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().
# Последняя строка входного файла обязательно заканчивается символом '\n'.

fin = open("input.txt")
lines_list = fin.readlines()
print("".join(list(reversed(lines_list))).strip("\n"))