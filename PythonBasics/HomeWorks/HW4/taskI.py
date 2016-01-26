# -*- coding: utf-8 -*
# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке.

# Выходные данные
# Выведите ответ на задачу.

list_numbers = input().split()

for index in range(0, len(list_numbers) - 1, 2):
    list_numbers[index], list_numbers[index + 1] = list_numbers[index + 1], list_numbers[index]

for number in list_numbers:
    print(number)