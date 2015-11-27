# -*- coding: utf-8 -*
# Простой неориентированный граф задан матрицей смежности,
# выведите его представление в виде списка ребер.

# Формат ввода
# Входные данные включают число n ( из отрезка [1;100]) – количество вершин в графе,
#  а затем n строк по n чисел, каждое из которых равно 0 или 1, – его матрицу смежности.

# Формат вывода
# Выведите список ребер заданного графа (в любом порядке).

def ReadSquareArray(line_number):
    A = []
    for i in range(line_number):
        A.append(list(map(int, input().strip().split())))
    return A


def MatrixToEdgeList(A, line_number):
    for i in range(line_number):
        for j in range(line_number):
            if A[i][j] == 1:
                A[j][i] = 0
                print(i + 1, j + 1)

line_number = int(input().strip())
A = ReadSquareArray(line_number)
MatrixToEdgeList(A, line_number)
