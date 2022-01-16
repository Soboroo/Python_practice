a=[list(map(int,input().split())) for _ in range(2)]
if a[1][0]<0 and a[1][1] >= 10:
    print('A storm warning for tomorrow! Be careful and stay home if possible!')
elif a[1][0]<a[0][0]:
    print('MCHS warns! Low temperature is expected tomorrow.')
elif a[1][1]>a[0][1]:
    print('MCHS warns! Strong wind is expected tomorrow.')
else:
    print('No message')