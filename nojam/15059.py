a=list(map(int, input().split()))
b=list(map(int, input().split()))
for i in range(len(a)):
    b[i] -= a[i]
    if b[i] < 0:
        b[i] = 0
print(sum(b))