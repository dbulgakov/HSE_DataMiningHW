tmp = input()
input_numbers = list(map(int, input().strip().split()))
min = input_numbers[0]
min2 = input_numbers[1]

for i in input_numbers:
    if i < min:
        min = i
for i in input_numbers:
    if i < min2 and i != min:
        min2 = i
print(min, min2)