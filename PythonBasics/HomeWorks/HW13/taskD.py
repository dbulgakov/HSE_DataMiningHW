# -*- coding: utf-8 -*
# На шахматной доске NxN в клетке (x1, y1) стоит голодный шахматный конь.
# Он хочет попасть в клетку (x2, y2), где растет вкусная шахматная трава.
# Какое наименьшее количество ходов он должен для этого сделать?

# Формат ввода
# На вход программы поступает пять чисел: N, x1, y1, x2, y2 (5 <= N <= 20, 1 <= x1, y1, x2, y2 <= N).
# Левая верхняя клетка доски имеет координаты (1, 1), правая нижняя - (N, N).

# Формат вывода
# Выведите единственное число K - наименьшее необходимое число ходов коня.


class Coordinate:
    def __init__ (self, crd_list):
          self.x = crd_list[0] - 1
          self.y = crd_list[1] - 1

possible_m = [(1, 2), (-1, -2), (2, 1), (-2, -1), (-1, 2), (1, -2), (-2, 1), (2, -1)]

board_size = int(input())

p1 = Coordinate(list(map(int, input().split())))
p2 = Coordinate(list(map(int, input().split())))

board = [[-1 for x in range(board_size)] for y in range(board_size)]
board[p1.x][p1.y] = 0

counter = 0

while board[p2.x][p2.y] == -1:
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == counter:
                for move in possible_m:
                    tmp_x = x + move[0]
                    tmp_y = y + move[1]
                    if tmp_x >= 0 and tmp_y >= 0 and tmp_x < board_size and tmp_y < board_size:
                        if board[tmp_x][tmp_y] == -1:
                            board[tmp_x][tmp_y] = counter + 1
    counter += 1

print(board[p2.x][p2.y])

