fin = open("input.txt")
lines_list = fin.readlines()

n = int(lines_list[0])
set_numbers = set(range(1, n))
set_numbers2 = {}

print(set_numbers)
counter = 0
while (True):
    if lines_list[counter] == "HELP":
        break
    if lines_list[counter] == "YES":
        print(lines_list[counter-1])
        set_numbers2 = set_numbers.union(set(lines_list[counter-1].split()))
    counter+=1

for item in set_numbers.intersection(set_numbers2):
    print(item)

#  считать из файла все множества с YES
# пересечь с исходным
# вывести элементы
# нет времени:C
