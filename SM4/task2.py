x = {'privet' : 'poka', 3:10}
x[3] = 'xxx'
print(x)

#если не хотим чтобы эксепшн

print(x.get(3, "zzzzzzzzzzzzzzzzzzzzzzzzz"))
#типо если нет - получаем зззззззззззз

