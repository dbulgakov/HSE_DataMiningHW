# -*- coding: utf-8 -*
# Реализуйте алгоритм бинарного поиска.

# Формат ввода
# В первой строке входных данных содержатся натуральные числа N и K (0 < N,K ≤ 100000 ).
# Во второй строке задаются N элементов первого массива, отсортированного по возрастанию,
# а в третьей строке – K элементов второго массива.
# Элементы обоих массивов - целые числа, каждое из которых по модулю не превосходит 109.

# Формат вывода
# Требуется для каждого из K чисел вывести в отдельную строку "YES",
# если это число встречается в первом массиве, и "NO" в противном случае.


def isInList(list, number):
    a = 0
    b = len(list)
    while True:
        if a == b:
           return "NO"
        middle = (a + b) // 2
        if list[middle] == number:
            return "YES"
        if list[middle] < number:
            a = middle + 1
        else:
            b = middle

len_arr = list(map(int, input().strip().split()))
input_numbers = list(map(int, input().strip().split()))
input_queries = list(map(int, input().strip().split()))

for number in input_queries:
    print(isInList(input_numbers, number))