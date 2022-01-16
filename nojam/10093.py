n,m=map(int,input().split())
print(max(0,m-n-1))
print(' '.join(map(str,list(range(n+1,m)))))