from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)
for i in range(int(input())):
    n, m = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    graph = [[] * (n + 1) for _ in range(n + 1)]
    preNodes = [[] for i in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        preNodes[b].append(a)
    w = int(input())

    tSort = []
    def dfs(v):
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                dfs(i)

        tSort.append(v)

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            dfs(i)

    tSort.reverse()
    #print(preNodes)
    #print(tSort)

    costSum = [0 for i in range(n + 1)]
    for i in tSort:
        if len(preNodes[i]) == 0:
            costSum[i] = cost[i]
        else:
            costSum[i] = cost[i] + max([costSum[j] for j in preNodes[i]])

    print(costSum[w])