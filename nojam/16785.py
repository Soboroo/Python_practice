a, b, c = map(int, input().split())
d = 0
e = 0
while True:
    e += 1
    d += a
    if not e % 7:
        d += b
    if d >= c:
        print(e)
        exit()