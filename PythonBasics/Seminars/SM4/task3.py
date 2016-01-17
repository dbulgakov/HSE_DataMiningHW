# Na prostie m-li

n = int(input())

s = set

for i in range (1, n ** (1/2)):
    c  = 0
    for j in s:
        if j % i == 0:
            c = c + i
            break
    if (c == 0):
        s.add(i)