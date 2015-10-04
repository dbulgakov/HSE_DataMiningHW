# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке.

# Выходные данные
# Выведите ответ на задачу.

numbers_list = input().split(" ")
for index in range(1, len(numbers_list)):
    if int(numbers_list[index]) > int(numbers_list[index - 1]):
        print(numbers_list[index])