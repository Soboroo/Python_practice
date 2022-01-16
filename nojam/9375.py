from itertools import product

for i in range(int(input())):
    d = dict()
    for j in range(int(input())):
        a, b = input().split()
        if b in d:
            d[b].append(a)
        else:
            d[b] = [a]

    print(d)
    print(list(product(*d.values())))