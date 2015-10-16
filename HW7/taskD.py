# -*- coding: utf-8 -*
# Выведите в обратном порядке содержимое всего файла полностью.
# Для этого считайте файл целиком при помощи метода read().

fin = open("input.txt")
big_string = fin.read()
print(big_string[::-1])