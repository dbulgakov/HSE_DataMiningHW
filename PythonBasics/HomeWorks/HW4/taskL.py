# -*- coding: utf-8 -*
# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке.

# Выходные данные
# Выведите ответ на задачу.


numbers_list = list(map(int, input().split()))
min_i = numbers_list.index(min(numbers_list))
max_i = numbers_list.index(max(numbers_list))
numbers_list[min_i], numbers_list[max_i] = numbers_list[max_i], numbers_list[min_i]
for number in list(map(str, numbers_list)):
    print(number)