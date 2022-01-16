from math import dist
from sys import stdin
for i in range(int(input())):
    a = [list(map(int, stdin.readline().split())) for i in range(4)]
    a.sort(reverse=True)
    tmp = a[-1]
    a[-1] = a[-2]
    a[-2] = tmp
    x = []
    y = []
    for j in range(4):
        x.append(dist(a[j], a[(j + 1) % 4]))
        y.append(dist(a[j], a[(j + 2) % 4]))
    print(1 if len(set(x)) == 1 and len(set(y)) == 1 else 0)
