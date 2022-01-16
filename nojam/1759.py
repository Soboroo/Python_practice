from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
a = stdin.readline().split()
a.sort()

q = deque()
x = ['a', 'i', 'u', 'e', 'o']


def backtrace(index):
    if len(q) == n:
        cnt = 0
        for i in q:
            for j in x:
                if i == j:
                    cnt += 1
        if cnt >= 1 and n - cnt >= 2:
            print(''.join(q))
    else:
        for i in range(index+1, m):
            if len(q) == 0 or q[-1] != a[i]:
                q.append(a[i])
                backtrace(i)
                q.pop()


backtrace(-1)