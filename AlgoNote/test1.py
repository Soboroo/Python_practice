from sys import stdin

for i in range(int(input())):
    a, b = map(int, stdin.readline().split())
    c, d = map(int, stdin.readline().split())
    while not a % 10:
        a //= 10
        b += 1
    while not c % 10:
        c //= 10
        d += 1
    tmp = min(b, d)
    b -= tmp
    d -= tmp
    print(a, b, c, d)