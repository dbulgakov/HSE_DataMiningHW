def IsPrime(n):
    if n==0:
        return(True)
    elif (n % 10) in [2,3,5,7]:
        return (IsPrime(n // 10))
    return(False)

n = int(input())

if (IsPrime(n)):
    print("YES")
else:
    print("NO")
