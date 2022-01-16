a = list(map(int, input().split()))
print('S' if len(set(a)) < 3 or sum(a) == max(a)*2 else 'N')