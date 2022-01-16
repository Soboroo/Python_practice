n = int(input())
result = [1 for i in range(n)]
a = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))