tmp = input().strip()
numbers = map(int, input().strip().split())
find_nub = int(input())
counter = 0
for i in numbers:
    if i == find_nub:
        counter += 1
print(counter)
