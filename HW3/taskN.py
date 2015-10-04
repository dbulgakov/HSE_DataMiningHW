# -*- coding: utf-8 -*
# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.

# Входные данные
# Дано число N, далее N-1 номер оставшихся карточек (различные числа от 1 до N).

# Выходные данные
# Программа должна вывести номер потерянной карточки.

number = int(input())
sum_input = 0

for i in range(1, number):
    temp_number = int(input())
    sum_input = sum_input + temp_number

sum_elements = (number * (number + 1)) // 2
print(sum_elements - sum_input)