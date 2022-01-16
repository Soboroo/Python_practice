from collections import deque
from sys import stdin

a,b = map(int, input().split())
graph = [[] for _ in range(a+1)]
postNode = [0 for _ in range(a+1)]
q = deque()
for _ in range(b):
    x,y=map(int,stdin.readline().split())
    graph[x].append(y)
    postNode[y] += 1 # postNode 개수에 따른 다음 노드 탐색 결정

for i in range(1,a+1):
    if postNode[i] == 0:
        q.append(i)

for i in range(a):
    x = q.popleft()
    print(x, end=' ')
    for j in graph[x]:
        postNode[j]-=1
        if postNode[j] == 0:
            q.append(j)