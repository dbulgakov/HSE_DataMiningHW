# -*- coding: utf-8 -*
# Реализуйте структуру данных "дек".
# Напишите программу, содержащую описание дека и моделирующую работу дека,
# реализовав все указанные здесь методы.
# Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию.
# После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:

# push_front
# Добавить (положить) в начало дека новый элемент. Программа должна вывести ok.
# push_back
# Добавить (положить) в конец дека новый элемент. Программа должна вывести ok.
# pop_front
# Извлечь из дека первый элемент. Программа должна вывести его значение.
# pop_back
# Извлечь из дека последний элемент. Программа должна вывести его значение.
# front
# Узнать значение первого элемента (не удаляя его). Программа должна вывести его значение.
# back
# Узнать значение последнего элемента (не удаляя его). Программа должна вывести его значение.
# size
# Вывести количество элементов в деке.
# clear
# Очистить дек (удалить из него все элементы) и вывести ok.
# exit
# Программа должна вывести bye и завершить работу.

# Гарантируется, что количество элементов в деке в любой момент не превосходит 100.
# Все операции pop_front, pop_back, front, back всегда корректны.

# Формат ввода
# Вводятся команды управления деком, по одной на строке.

# Формат вывода
# Требуется вывести протокол работы дека, по одному сообщению на строке.

def push_front(deque, number):
    deque.insert(0, number)
    print("ok")


def push_back(deque, number):
    deque.append(number)
    print("ok")


def pop_front(deque):
    print(deque.pop(0))


def pop_back(deque):
    print(deque.pop())


def front(deque):
    print(deque[0])


def back(deque):
    print(deque[len(deque) - 1])


def size(deque):
    print(len(deque))


def clear(deque):
    deque[:] = []
    print("ok")

deque = []

while (True):
    input_cmd = input().strip().split()
    function = input_cmd[0]
    if function == "exit":
        print("bye")
        break
    elif function == "push_front":
        push_front(deque, input_cmd[1])
    elif function == "push_back":
        push_back(deque, input_cmd[1])
    elif function == "pop_front":
        pop_front(deque)
    elif function == "pop_back":
        pop_back(deque)
    elif function == "front":
        front(deque)
    elif function == "back":
        back(deque)
    elif function == "size":
        size(deque)
    elif function == "clear":
        clear(deque)