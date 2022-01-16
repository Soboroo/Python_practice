n=int(input())
for i in range(1,2 * n):
    print(' '*abs(i-n),end='')
    print('*'*(-abs(i-n)+n))