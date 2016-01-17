a = int(input())
b = int(input())

if (a == b and int(str(a)[2:][::-1]) == int(str(a)[:-2])):
    print(a)
else:
    for i in range(a, b+1):
        if int(str(i)[2:][::-1]) == int(str(i)[:-2]):
            print(i)