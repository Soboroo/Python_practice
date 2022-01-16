from sys import stdin
for i in range(int(input())):
    a = int(stdin.readline())
    delta = [25, 10, 5, 1]
    for j in range(4):
        tmp = delta[j]
        delta[j] = a // delta[j]
        a %= tmp
    print(" ".join(list(map(str, delta))))