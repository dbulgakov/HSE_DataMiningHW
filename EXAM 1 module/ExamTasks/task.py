import math
A = int(input())
B = int(input())
i = min(A, B)
while i <= max(A,B):
    a1 = i/1000
    a2 = (i/100)%10
    a3 = (i/10)%10
    a4 = i%10
if a1 == a2 == a3 or a2 == a3 == a4 or a1 == a3 == a4 or a1 == a2 == a4:
print(i)
i = i + 1