# -*- coding: utf-8 -*
# Дана строка. Получите новую строку, вставив между двумя символами исходной строки символ *. Выведите полученную строку.

# Входные данные
# Вводится строка.

# Выходные данные
# Выведите ответ на задачу.

input_string = input();
output_string = ""
for letter in input_string:
    output_string = output_string + letter + "*"
print(output_string[:-1])