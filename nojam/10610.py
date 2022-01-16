a = sorted(list(input()), reverse=True)
print(-1 if not a.count('0') or sum(list(map(int, a))) % 3 else ''.join(a))
