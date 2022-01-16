from sys import stdin

g = list()
mod = 1000000007
for i in range(int(input())):
    a, b = map(int, stdin.readline().split())
    a *= b
    b -= 1
    g.append((a, b))


def power(x, y):
    if y < 0:
        return 0
    elif y == 0:
        return 1
    elif y == 1:
        return x
    flag = y % 2
    if flag:
        y -= 1
    r = power(x, y // 2) % mod
    return r * r * (x if flag else 1) % mod

print(sum(map(lambda x: x[0] * power(2, x[1]), g)) % mod)
