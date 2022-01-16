n = int(input())
a = []
for i in range(n):
    for j in range(10):
        if len(a) == 0 or a[-1] < j:
            a.append(j)
        