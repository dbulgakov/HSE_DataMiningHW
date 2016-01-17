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

def mergesort(x):
    if len(x) <= 1:
        return x

    m = len(x) // 2
    z = mergesort(x[:m])
    v = mergesort(x[m:])
    return merge(z, v)

x = [1, 2, 90, 20, -10, 0]
print(mergesort(x))