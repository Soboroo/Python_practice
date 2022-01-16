n=int(input())
a = [list(input()) for i in range(n)]
for i in range(len(a[0])):
    flag = True
    for j in range(1, n):
        if a[0][i] != a[j][i]:
            flag = False
    print(a[0][i] if flag else '?', end='')