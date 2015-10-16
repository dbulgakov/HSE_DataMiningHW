# -*- coding: utf-8 -*
# Выведите в обратном порядке содержимое всего файла полностью.
# Для этого считайте файл целиком при помощи метода read().

fin = open("input.txt")
big_string = fin.read()
f_out = open("output.txt", "w")
print(big_string[::-1], file=f_out)
fin.close()
f_out.close()