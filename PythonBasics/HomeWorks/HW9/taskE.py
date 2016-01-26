# -*- coding: utf-8 -*
# Дан список целых чисел. Отсортируйте его в порядке невозрастания значений.
# Выведите полученный список на экран.
# Решите эту задачу при помощи алгоритма пузырьковой сортировки.
# Решение оформите в виде функции BubbleSort(A).

# Формат ввода
# Данные вводятся с клавиатуры или из файла input.txt.

# Формат вывода
# Данные выводятся на экран или в файл output.txt.

def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if int(A[j]) > int(A[j - 1]):
                A[j], A[j - 1] = A[j - 1], A[j]
    return A

input_numbers = input().split()
for item in BubbleSort(input_numbers):
    print(item)
