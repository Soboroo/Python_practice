from sys import stdin
n = list(stdin.readline().rstrip())
k = stdin.readline().strip()
m = []
for i in n:
    m.append(i)
    if ''.join(m[-len(k):]) == k:
        for j in range(len(k)):
            m.pop()

print(''.join(m) if len(m) else 'FRULA')