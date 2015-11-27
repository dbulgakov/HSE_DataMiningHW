# -*- coding: utf-8 -*
# Простой неориентированный граф задан матрицей смежности. Найдите количество ребер в графе.

# Формат ввода
# На вход программы поступает число n ( из отрезка [0;100]) – количество вершин в графе,
# а затем n строк по n чисел, каждое из которых равно 0 или 1, – его матрица смежности.

# Формат вывода
# Выведите одно число – количество ребер заданного графа.


def ReadSquareArray(line_number):
    A = []
    for i in range(line_number):
        A.append(list(map(int, input().strip().split())))
    return A


def CountNumberOfEdges(A):
    tmp_s = 0
    for l in A:
        tmp_s += sum(l)
    return tmp_s // 2

line_number = int(input().strip())
A = ReadSquareArray(line_number)

print(CountNumberOfEdges(A))