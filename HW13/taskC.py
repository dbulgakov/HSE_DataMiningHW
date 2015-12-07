# -*- coding: utf-8 -*
# В неориентированном графе требуется найти минимальный путь между двумя вершинами.

# Формат ввода
# Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100).
# Затем записана матрица смежности (0 обозначает отсутствие ребра, 1 – наличие ребра).
#  Далее задаются номера двух вершин – начальной и конечной.

# Формат вывода
# Выведите L – длину кратчайшего пути (количество ребер, которые нужно пройти). Если пути нет, нужно вывести -1.

def ReadSquareArray(line_number):
    A = []
    for i in range(line_number):
        A.append(list(map(int, input().strip().split())))
    return A


def bfs(start, end, v_number):
    D = [None] * v_number
    D[start] = 0
    Q = [start]
    Qstart = 0
    while Qstart < len(Q):
        u = Q[Qstart]
        Qstart += 1
        for v in range(v_number):
            if D[v] is None and road_list[u][v] == 1:
                D[v] = D[u] + 1
                Q.append(v)
    return D[end]

v_number = int(input().strip())

road_list = ReadSquareArray(v_number)

data_tmp = list(map(int, input().split()))
start = data_tmp[0] - 1
end = data_tmp[1] - 1
if bfs(start, end, v_number) is None:
    print("-1")
else:
    print(bfs(start, end, v_number))