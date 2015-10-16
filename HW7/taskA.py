# -*- coding: utf-8 -*
# Во входном файле записано два целых числа, каждое в отдельной строке.
# Выведите в выходной файл их сумму.

fin = open("input.txt")
numbers_list = list(map(int, fin.read().split()))
print(sum(numbers_list))
f_out = open("output.txt", "w")
f_out.write(str(sum(numbers_list)))
fin.close()
f_out.close()