# -*- coding: utf-8 -*
# Выведите все четные элементы списка.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке.

# Выходные данные
# Выведите ответ на задачу.

numbers_list = input().split(" ")
for number in numbers_list:
    if int(number) % 2 == 0:
        print(number)