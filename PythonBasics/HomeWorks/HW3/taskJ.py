# -*- coding: utf-8 -*
# Квадрат трехзначного числа оканчивается тремя цифрами, равными этому числу. Найдите и выведите все такие числа.

# Входные данные
# Программа не требует ввода данных с клавиатуры, просто выводит список искомых чисел.

# Выходные данные
# Выведите ответ на задачу.

for i in range(100,1000):
    str_number = str(i ** 2)
    if i == int(str_number[-3:]):
        print(i)