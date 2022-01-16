from math import ceil
a=list(map(int,input().split()))
print(min(ceil(a[0]/a[1])*a[2],ceil(a[0]/a[3])*a[4]))