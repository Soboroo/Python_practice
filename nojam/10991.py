n=int(input())
for i in range(n):
    print(' '*(-i+n-1),end='')
    for j in range(2*i+1):
        print(' 'if j%2else'*',end='')
    print()