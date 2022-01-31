from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    a = list(map(int, input().split()))
    for i in range(1, len(a), 2):
        if a[i] == -1:
            break
        graph[a[0]].append((a[i], a[i + 1]))

max_distance = 0
max_distance_node = 0


def dfs(node, distance, visited):
    global max_distance, max_distance_node
    if distance > max_distance:
        max_distance = distance
        max_distance_node = node
    for i in range(len(graph[node])):
        if not visited[graph[node][i][0]]: # in 연산자 O(n) vs list 참조 O(1)
            visited[graph[node][i][0]] = True
            dfs(graph[node][i][0], distance + graph[node][i][1], visited)


visited = [False] * (n + 1)
visited[1] = True
dfs(1, 0, visited)

visited = [False] * (n + 1)
visited[max_distance_node] = True
dfs(max_distance_node, 0, visited)

print(max_distance)

