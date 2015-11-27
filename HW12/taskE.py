# -*- coding: utf-8 -*
# Неориентированный граф задан матрицей смежности. Найдите степени всех вершин графа.

# Формат ввода
# Сначала вводится число n ( из отрезка [0;100]) – количество вершин в графе,
# а затем n строк по n чисел, каждое из которых равно 0 или 1, – его матрица смежности.

# Формат вывода
# Выведите n чисел – степени вершин графа.

def ReadSquareArray(line_number):
    A = []
    for i in range(line_number):
        A.append(list(map(int, input().strip().split())))
    return A


def DegOfVerticles(A):
    for line in A:
        print(sum((line)))

line_number = int(input().strip())
A = ReadSquareArray(line_number)

DegOfVerticles(A)