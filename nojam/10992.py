n=int(input())
for i in range(n-1):
    print(' '*(-i+n-1), end='')
    print('*', end='')
    print(' '*(2*i-1), end='')
    print('*' if i > 0 else '')
print('*'*(2*n-1))