input_string = input()
if len(input_string) % 2 == 0:
    first_part = input_string[:len(input_string)//2]
else:
    first_part = input_string[:len(input_string)//2 + 1]
final_string = input_string.replace(first_part, "") + first_part

print(final_string)