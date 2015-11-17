def isInList(list, number):
    a = 0
    b = len(list)
    while True:
        if a == b:
           return "NO"
        middle = (a + b) // 2
        if list[middle] == number:
            return "YES"
        if list[middle] < number:
            a = middle + 1
        else:
            b = middle

len_arr = list(map(int, input().strip().split()))
input_numbers = list(map(int, input().strip().split()))
input_queries = list(map(int, input().strip().split()))

for number in input_queries:
    print(isInList(input_numbers, number))