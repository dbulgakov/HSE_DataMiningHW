fin = open("input.txt")
filelines_list = fin.readlines()

number_lines = int(list(filelines_list[0].split())[0])
number_rows = int(list(filelines_list[0].split())[1])
number_queries = int(list(filelines_list[0].split())[2])

elements_matrix = list()

for line_number in range(1, number_lines + 1):
    elements_matrix.append(list(map(int, filelines_list[line_number].split())))

queries_matrix = list();

for line_number in range(number_lines + 1, len(filelines_list)):
    queries_matrix.append(list(map(int, filelines_list[line_number].split())))

result_list = list()

print(queries_matrix)

for i in range(0, number_queries):
    s = 0
    for j in range(queries_matrix[i][0] - 1, queries_matrix[i][2]):
        for k in range(queries_matrix[i][1] - 1, queries_matrix[i][3]):
            s = s + elements_matrix[j][k]
    result_list.append(s)

f_out = open("output.txt", "w")
result_list = map(str, result_list)
print(("\n".join(result_list)), file=f_out)
fin.close()
f_out.close()