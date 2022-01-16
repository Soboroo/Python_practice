from math import ceil
input()
a = list(map(int, input().split()))
x, y = map(int, input().split())
print(sum(map(lambda f: 1+ceil((f-x if f-x >= 0 else 0) / y), a)))