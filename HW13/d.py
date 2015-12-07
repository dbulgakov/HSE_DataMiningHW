def bfs(start, end):
    prev = [None] * n
    prev[start] = 0
    queue = [start]
    queue_start = 0
    while queue_start < len(queue):
        current_vertex = queue[queue_start]
        queue_start += 1
        for v in range(n):
            if prev[v] is None and adj_matrix[current_vertex][v] == 1:
                prev[v] = prev[current_vertex] + 1
                queue.append(v)
    return prev[end]


n = int(input())
adj_matrix = [[] for i in range(n)]
for i in range(n):
    line = input().split()
    adj_matrix[i] = [int(v) for v in line]
a = list(map(int, input().split()))
start_vertex = a[0] - 1
end_vertex = a[1] - 1
if bfs(start_vertex, end_vertex) is None:
    print(-1)
else:
    print(bfs(start_vertex, end_vertex))