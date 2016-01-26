# -*- coding: utf-8 -*
# Даны два целых числа A и B (при этом A≤B). Выведите все числа от A до B включительно.

# Входные данные
# Вводятся два целых числа.

# Выходные данные
# Выведите ответ на задачу.

start_num = int(input())
finsih_num = int(input())
for n in range (start_num, finsih_num+1):
    print(n)