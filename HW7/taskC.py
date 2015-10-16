# -*- coding: utf-8 -*
# Выведите все строки данного файла в обратном порядке.
# Для этого считайте список всех строк при помощи метода readlines().
# Последняя строка входного файла обязательно заканчивается символом '\n'.

fin = open("input.txt")
lines_list = fin.readlines()
f_out = open("output.txt", "w")
print("".join(list(reversed(lines_list))).strip("\n"), file=f_out)
fin.close()
f_out.close()