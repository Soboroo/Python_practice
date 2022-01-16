from sys import stdin
input=stdin.readline
n=int(input())
a=list(map(int,input().split()))
m=[0]*n
for i in range(1, n):
    a[i]+=a[i-1]
    m[i]=min(m[i-1],a[i-1])
print(max(a[0],max([a[i]-m[i]for i in range(1,n)])))