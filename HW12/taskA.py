# -*- coding: utf-8 -*
# По заданной квадратной матрице n×n из нулей и единиц определите,
# может ли данная матрица быть матрицей смежности простого неориентированного графа.

# Формат ввода
# На вход программы поступает число n ( из отрезка [1; 100]) – размер матрицы,
# а затем n строк по n чисел, каждое из которых равно 0 или 1, – сама матрица.

# Формат вывода

# Выведите «YES», если приведенная матрица может быть матрицей смежности
# простого неориентированного графа, и «NO» в противном случае.


def ReadSquareArray(line_number):
    A = []
    for i in range(line_number):
        A.append(list(map(int, input().strip().split())))
    return A


flg = True
line_number = int(input().strip())
A = ReadSquareArray(line_number)
for i in range (0, line_number):
    for j in range(0, line_number):
        if i == j:
            if A[i][j] != 0:
                flg = False
        else:
            if A[i][j] != A[j][i]:
                flg = False

print("YES" if flg else "NO")