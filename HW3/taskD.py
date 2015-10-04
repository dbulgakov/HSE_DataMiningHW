# -*- coding: utf-8 -*

# По данным целым неотрицательным n и k вычислите значение числа сочетаний из n элементов по k, то есть n!/(k!(n−k)!).

# Входные данные
# Вводятся числа n и k.

# Выходные данные
# Выведите ответ на задачу.

import math
n = int(input())
k = int(input())

comb = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

print(int(comb))