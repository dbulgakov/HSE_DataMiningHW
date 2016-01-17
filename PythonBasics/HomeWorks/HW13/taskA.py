# -*- coding: utf-8 -*
# Дан неориентированный невзвешенный граф. Для него вам необходимо найти количество вершин, лежащих в одной компоненте
# связности с данной вершиной (считая эту вершину).

# Формат ввода
# В первой строке входных данных содержатся два числа: N и S (1 <= N <= 100; 1 <= S <= N),
# где N – количество вершин графа, а S – заданная вершина.8
# В следующих N строках записано по N чисел – матрица смежности графа,
# в которой 0 означает отсутствие ребра между вершинами,
# а 1 – его наличие. Гарантируется, что на главной диагонали матрицы всегда стоят нули.

# Формат вывода
# Выведите одно целое число – искомое количество вершин.


def ReadSquareArray(line_number):
    A = []
    for i in range(line_number):
        A.append(list(map(int, input().strip().split())))
    return A


input_data = list(map(int, input().strip().split()))
vertex_number = input_data[0]
starting_vertex = input_data[1]

matrix = ReadSquareArray(vertex_number)

visited = set()
n = 1

def dfs(v):
    global n
    visited.add(v)
    for iter in range(vertex_number):
        if matrix[v][iter] == 1 and iter not in visited:
            n += 1
            dfs(iter)
    return n
print(dfs(starting_vertex - 1))