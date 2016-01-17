# -*- coding: utf-8 -*
# Дан неориентированный невзвешенный граф.
# Необходимо посчитать количество его компонент связности и вывести их.

# Формат ввода
# Во входном файле записано два числа N и M (0 < N ≤ 100000, 0 ≤ M ≤ 100000).
# В следующих M строках записаны по два числа i и j (1 ≤ i, j ≤ N),
# которые означают, что вершины i и j соединены ребром.

# Формат вывода
# В первой строчке выходного файла выведите количество компонент связности.
# Далее выведите сами компоненты связности в следующем формате: в первой строке количество вершин в компоненте,
#  во второй - сами вершины в порядке возрастания.


nm_lst = list(map(int, input().strip().split()))
n = nm_lst[0]
m = nm_lst[1]

edg = [0] * n
comp = [0] * n
was = [0] * n
for i in range(n):
        edg[i] = []
        comp[i] = []

for i in range(m):
        tmp_list = list(map(int, input().strip().split()))
        u = tmp_list[0] - 1
        v = tmp_list[1] - 1
        edg[u].append(v)
        edg[v].append(u)

res = 0

def dfs(v):
        was[v] = 1
        comp[res - 1].append(str(v + 1))
        for i in edg[v]:
                if was[i] == 0:
                        dfs(i)

for i in range(n):
        if was[i] == 0:
                res += 1
                dfs(i)


print(res)
for i in range(res):
    print(str(len(comp[i])))
    print(" ".join(comp[i]))