from collections import deque


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


a = list(map(int, input().split()))
visited = [False for i in range(a[0]+1)]
graph = [[]for i in range(a[0]+1)]
for i in range(a[1]):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(a[0]+1):
    graph[i].sort()
dfs(a[2])
print()
visited = [False for i in range(a[0]+1)]
bfs(a[2])
