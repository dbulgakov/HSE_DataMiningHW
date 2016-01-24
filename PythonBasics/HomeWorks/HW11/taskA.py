# -*- coding: utf-8 -*
# Реализуйте структуру данных стек.
# Напишите программу, содержащую описание стека и моделирующую работу стека,
# реализовав все указанные здесь методы.
# Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию.
# После выполнения каждой команды программа должна вывести одну строчку.

# Возможные команды для программы:
# 1) push n
# Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.
# 2) pop
# Удалить из стека последний элемент. Программа должна вывести его значение.
# 3) back
# Программа должна вывести значение последнего элемента, не удаляя его из стека.
# 4) size
# Программа должна вывести количество элементов в стеке.
# 5) clear
# Программа должна очистить стек и вывести ok.
# 6) exit
# Программа должна вывести bye и завершить работу.

# Формат ввода
# Команды управления стеком вводятся в описанном ранее формате по 1 на строке.
# Гарантируется, что набор входных команд удовлетворяет следующим требованиям:
# максимальное количество элементов в стеке в любой момент не превосходит 100,
# все команды pop и back корректны, то есть при их исполнении в стеке содержится хотя бы один элемент.

# Формат вывода
# Требуется вывести протокол работы со стеком, по 1 сообщению в строке.





def push(stack, number):
    stack.append(number)
    print("ok")


def pop(stack):
    print(stack.pop())


def back(stack):
    print(stack[-1])


def size(stack):
    print(len(stack))


def clear(stack):
    stack[:] = []
    print("ok")

stack = []

while (True):
    input_cmd = input().strip().split()
    function = input_cmd[0]
    if function == "exit":
        print("bye")
        break
    elif function == "push":
        push(stack, input_cmd[1])
    elif function == "pop":
        pop(stack)
    elif function == "back":
        back(stack)
    elif function == "size":
        size(stack)
    elif function == "clear":
        clear(stack)