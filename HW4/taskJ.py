# -*- coding: utf-8 -*
# Дана строка, в которой буква h встречается как минимум два раза.
# Разверните последовательность символов, заключенную между первым и последнием появлением буквы h, в противоположном порядке.

# Входные данные
# Вводится строка.

# Выходные данные
# Выведите ответ на задачу.

input_string = input()
start_intex = input_string.index("h")
end_index = input_string.rindex("h")
substring = input_string[start_intex:end_index + 1]
print(input_string.replace(substring, substring[::-1]))