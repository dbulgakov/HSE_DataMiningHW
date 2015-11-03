input_number = int(input())

sum_numbers = 2
output_string = "1*2+"
for i in range(2, input_number):
    sum_numbers = sum_numbers + i * (i + 1)
    output_string = output_string + str(i) + "*" + str(i+1) + "+"
print(output_string[:-1] + "=" + str(sum_numbers))