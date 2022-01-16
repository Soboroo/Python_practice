a, b, c = map(int, input().split())
if b <= a <= c:
    print(a)
elif a > c:
    print(c)
else:
    print(b)