n = int(input())
result = [1 for i in range(n)]
a = list(map(int, input().split()))

for i in range(1, n):
    state = 0 if a[0] < a[1] else 1
    flag = False
    for j in range(i):
        if state == 0 and a[j] > a[i]:
            state = 1
            flag = True
        if state == 1 and a[j] < a[i]:
            state = 0
            flag = True
        if not flag and ((state == 0 and a[j] < a[i]) or (state == 1 and a[j] > a[i])):
            result[i] = max(result[i], result[j] + 1)

print(max(result))