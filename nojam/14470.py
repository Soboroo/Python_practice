a = [int(input()) for i in range(5)]
if a[0] < 0:
    print(-a[0] * a[2] + a[3] + a[1] * a[4])
else:
    print((a[1]-a[0])*a[4])