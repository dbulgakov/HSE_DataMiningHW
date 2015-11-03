a = [1, 3, 3, 10, 13, 123, 1234]
x = 123
l = 0
r = len(a) - 1
while r - l > 1:
    m = (r + 1) // 2
    if x >= a[m]:
        l = m
    else:
        r = m

if x == a[l] or x == a[r]:
    print("YES")
else:
    print("NO")