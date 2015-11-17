def LowerBound(list, number, dict):
    left = 0
    right = len(list) - 1
    if list[0] == number:
        return 0
    if number in dict:
        return dict[number]
    while left <= right:
        middle = (left + right) // 2
        if list[middle] > number:
            right = middle - 1
        elif list[middle] < number:
            left = middle + 1
        else:
            return GoBack(list, middle, number)
    return -1

def UpperBound (A, key, left):
    left = left
    right = len(A)
    while right > left + 1:
        middle = (left + right) // 2
        if A[middle] > key:
            right = middle
        else:
            left = middle
    return right

def GoBack(list, index, number):
    while list[index] == number and index > 0:
        index -= 1
    return index + 1


n,k = map(int, input().split())
input_numbers = list(map(int, input().strip().split()))
input_queries = list(map(int, input().strip().split()))
dict_n = dict()
for num in input_queries:
    tmp = LowerBound(input_numbers, num, dict_n)
    if tmp != -1:
        print(tmp + 1, UpperBound(input_numbers, num, tmp))
        dict_n[num] = tmp
    else:
        print("0")