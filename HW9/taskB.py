# -*- coding: utf-8 -*
# Дан список чисел. Определите, есть ли в нем два противоположных(то есть дающих в сумме 0) числа.
# Если такие числа есть в массиве, выведите их индексы в порядке возрастания.
# Если таких чисел в массиве нет, ничего не выводите. Гарантируется, что таких пар не больше одной.

# Формат ввода
# Данные вводятся с клавиатуры или из файла input.txt.

# Формат вывода
# Данные выводятся на экран или в файл output.txt.

def FindSameОppositeNumbers(A):
    index_list = []
    for i in range(0, len(A)):
        for k in range(i, len(A)):
            if A[i]+A[k] == 0:
                index_list.append(i)
                index_list.append(k)
    return index_list





input_numbers = list(map(int, input().split(" ")))
for item in FindSameОppositeNumbers(input_numbers):
    print(item)
