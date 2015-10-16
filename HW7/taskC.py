fin = open("input.txt")
lines_list = fin.readlines()
lines_list = lines_list.reverse()
print(''.join(lines_list).strip('\n'))
