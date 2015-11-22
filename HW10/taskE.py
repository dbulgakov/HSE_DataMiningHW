# -*- coding: utf-8 -*
# Дано два списка чисел, числа в первом списке упорядочены по неубыванию.
# Для каждого числа из второго списка определите номер первого
# и последнего появления этого числа в первом списке.

# Формат ввода
# В первой строке входных данных записано два числа N и M (1 ≤ N, M ≤ 20000 ).
# Во второй строке записано N упорядоченных по неубыванию целых чисел — элементы первого списка.
# В третьей строке записаны M целых неотрицательных чисел - элементы второго списка.
# Все числа в списках - целые 32-битные знаковые.

# Формат вывода
# Программа должна вывести M строчек.
# Для каждого числа из второго списка нужно вывести номер его первого
# и последнего вхождения в первый список. Нумерация начинается с единицы.
# Если число не входит в первый список, нужно вывести одно число 0.


def LowerBound(list, number, dict):
    left = 0
    right = len(list) - 1
    if list[0] == number:
        return 0
    if number in dict:
        return dict[number]
    while left <= right:
        middle = (left + right) // 2
        if list[middle] > number:
            right = middle - 1
        elif list[middle] < number:
            left = middle + 1
        else:
            return GoBack(list, middle, number)
    return -1

def UpperBound (list, number, left):
    left = left
    right = len(list)
    while right > left + 1:
        middle = (left + right) // 2
        if list[middle] > number:
            right = middle
        else:
            left = middle
    return right

def GoBack(list, index, number):
    while list[index] == number and index > 0:
        index -= 1
    return index + 1


n,k = map(int, input().split())
input_numbers = list(map(int, input().strip().split()))
input_queries = list(map(int, input().strip().split()))
dict_n = dict()
for num in input_queries:
    tmp = LowerBound(input_numbers, num, dict_n)
    if tmp != -1:
        print(tmp + 1, UpperBound(input_numbers, num, tmp))
        dict_n[num] = tmp
    else:
        print("0")