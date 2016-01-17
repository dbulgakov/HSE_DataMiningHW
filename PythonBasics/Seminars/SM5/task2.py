def merge(x, y):
    z = []
    a = 0
    b = 0
    while (a != len(x) and b != len(y)):
        if x[a] < y[b]:
            z.append(x[a])
            a += 1
        else:
            z.append(y[b])
            b += 1
    z += y[b:]
    z += x[a:]
    return z