x = {1, 2, 3, 4}
print(3 in x)
print(x.remove(2))
print(x)

for item in x:
    print(item)

    #| - объединение
    #& - пересечение


x = {1, 2, 3, 4}
y = {1, 2}

for e in x.union(y):
    print()

h = {'privet' : 'poka', 3:10}
print(x['privet'])