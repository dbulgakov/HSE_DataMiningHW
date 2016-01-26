# -*- coding: utf-8 -*
# Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли,
# что каждый элемент этого списка больше предыдущего).
# Выведите YES, если массив монотонно возрастает и NO в противном случае.
# Решение оформите в виде функции IsAscending(A).
# В данной функции должен быть один цикл while, не содержащий вложенных условий и циклов
# используйте схему линейного поиска.

# Формат ввода
# Данные вводятся с клавиатуры или из файла input.txt.

# Формат вывода
# Данные выводятся на экран или в файл output.txt.

def IsAscending(A):
    counter = 1
    flag = True
    while (counter < len((A))):
        flag = flag and A[counter - 1] < A[counter]
        counter += 1
    return flag

input_numbers = list(map(int, input().split(" ")))
if IsAscending(input_numbers):
    print("YES")
else:
    print("NO")