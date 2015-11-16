def findnumber(list, number):
    a = 0
    b = len(list) - 1
    while(True):
        middle = (a + b) // 2
        if number < list[middle]:
            b = middle
        elif number > list[middle]:
            a = middle
        else:
            return middle

tmp = input()
input_numbers = map(int, input().strip().split())
input_numbers = sorted(input_numbers)
number_to_find = int(input().strip())
print(findnumber(input_numbers, number_to_find))