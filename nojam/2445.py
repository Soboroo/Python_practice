n=int(input())
for i in range(1,2 * n):
    print('*'*(-abs(i-n)+n),end='')
    print(' '*2*abs(i-n),end='')
    print('*'*(-abs(i-n)+n))