def findnumber(list, number):
    c_num = list[0]
    for i in list:
        if abs(i - number) < abs (c_num - number):
            c_num = i
    return c_num

tmp = input()
input_numbers = list(map(int, input().strip().split()))
number_to_find = int(input().strip())
print(findnumber(input_numbers, number_to_find))