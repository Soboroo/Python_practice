n = int(input())
i = 0
m = 0
while i <= n:
    if m > 9876543210:
        print(-1)
        exit()
    if m < 10:
        i += 1
    else:
        flag = True
        for j in range(1, len(str(m))):
            if str(m)[j] >= str(m)[j-1]:
                flag = False
                break
        if flag:
            i += 1
    m += 1

print(m-1)