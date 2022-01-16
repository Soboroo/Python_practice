a = [int(input()) for i in range(3)]
r = 0
s = []
for i in range(3):
    r = 0
    for j in range(3):
        r += abs(i-j)*2*a[j]
    s.append(r)
print(min(s))