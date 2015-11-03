fin = open("input.txt")
filelines_list = fin.readlines()

first_line = filelines_list[0].split()
number_lines = int(first_line[0])
number_rows = int(first_line[1])
number_queries = int(first_line[2])

queries_matrix = list()

for line_number in range(number_lines + 1, len(filelines_list)):
    queries_matrix.append(filelines_list[line_number].split())

for query in queries_matrix:
    s = 0
    tmp_list = list()
    for i in range(int(queries_matrix[1][1]), int(queries_matrix[1][3])+1):
        tmp_list.append(filelines_list[i].split())

    for j in range(int(query[0])-1, int(query[2])):
        for k in range(int(query[1])-1, int(query[3])):
            s = s + int(tmp_list[j][k])
    print(s)