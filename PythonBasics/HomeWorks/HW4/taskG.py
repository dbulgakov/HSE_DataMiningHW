# -*- coding: utf-8 -*
# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.

# Входные данные
# Вводится строка.

# Выходные данные
# Выведите ответ на задачу.

input_string = input()
start_intex = input_string.index("h")
end_index = input_string.rindex("h")
substring = input_string[start_intex:end_index + 1]
print(input_string.replace(substring, ""))