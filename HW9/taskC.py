# -*- coding: utf-8 -*
# Дан список целых чисел.Выведите все элементы этого списка в порядке невозрастания значений.
# Выведите новый список на экран.
# Решите эту задачу при помощи алгоритма сортировки выбором.
# Решение оформите в виде функции SelectionSort(A).

# Формат ввода
# Данные вводятся с клавиатуры или из файла input.txt.

# Формат вывода
# Данные выводятся на экран или в файл output.txt.

def SelectionSort(A):
    for i in range(len(A)):
        biggest = i
        for k in range(i + 1, len(A)):
            if int(A[k]) > int(A[biggest]):
                biggest = k
        A[biggest], A[i] = A[i], A[biggest]
    return A

input_numbers = input().split()
for item in SelectionSort(input_numbers):
    print(item)