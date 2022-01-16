n=input().upper()
n=list(map(n.count, n))
print(n)
print(max(n) if n.count(max(n))==1 else '?')