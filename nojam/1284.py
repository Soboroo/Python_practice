while True:
    a = list(input().rstrip())
    if a == ['0']:
        exit()
    r = 1 + len(a)
    for i in a:
        if i == '1':
            r += 2
        elif i == '0':
            r += 4
        else:
            r += 3
    print(r)