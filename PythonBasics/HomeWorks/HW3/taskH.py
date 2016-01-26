# -*- coding: utf-8 -*
# Для данного числа n<100 закончите фразу “На лугу пасется...”
# одним из возможных продолжений: “n коров”, “n корова”, “n коровы”.
# правильно склоняя слово “корова”.

# Входные данные
# Вводится натуральное число.

# Выходные данные
# Программа должна вывести введенное число n и одно из слов: korov, korova или korovy.
# Между числом и словом должен стоять ровно один пробел.

cow_number = int(input())
if (cow_number >=10 and cow_number < 21):
    print(cow_number, "korov")
else:
    n = cow_number % 10
    if n == 1:
        print(cow_number, "korova")
    elif n > 0 and n < 5:
        print(cow_number, "korovy")
    else:
        print(cow_number, "korov")