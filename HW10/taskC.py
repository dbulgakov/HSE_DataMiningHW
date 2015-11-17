N = int(input())
list = list(map(int, input().strip().split()))

min1 = int(list[0])
min2 = int(list[1])

for number in list:
    if number < min1:
        min2 = min1
        min1 = number
    elif number < min2:
        min2 = number

print(min1, min2)