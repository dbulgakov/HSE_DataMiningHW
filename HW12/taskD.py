# -*- coding: utf-8 -*
# Простой неориентированный граф задан списком ребер,
# выведите его представление в виде матрицы смежности.

# Формат ввода
# На вход программы поступают числа n (из отрезка [1;100]) – количество вершин в графе
# и m ( из отрезка [1; n*(n-1)/2]) – количество ребер. Затем следует m пар чисел – ребра графа.

# Формат вывода
# Выведите матрицу смежности заданного графа.


def CreateMatrix(vertex_number):
    matrix = [0] * vertex_number
    for i in range(vertex_number):
        matrix[i] = [0] * vertex_number
    return matrix


def FillMatrixWithEdges(matrix, edge_number):
    for i in range(edge_number):
        tmp_list = list(map(int, input().strip().split()))
        matrix[tmp_list[0] - 1][tmp_list[1] - 1] = 1
        matrix[tmp_list[1] - 1][tmp_list[0] - 1] = 1
    return matrix


def PrintMatrix(matrix):
    for row in matrix:
        print(' '.join([str(elem) for elem in row]))

initial_data = list(map(int, input().strip().split()))
vertex_number = initial_data[0]
edge_number = initial_data[1]
matrix = CreateMatrix(vertex_number)
matrix = FillMatrixWithEdges(matrix, edge_number)

PrintMatrix(matrix)


