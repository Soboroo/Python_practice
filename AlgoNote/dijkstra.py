from sys import stdin

INF = int(1e9)

n, m = map(int, stdin.readline().split())
start = int(stdin.readline())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] #distance에 start로부터의 거리 기록
    for i in range(n-1):
        now = get_smallest_node() # 주변 노드중 비용이 가장 적은 노드 선택
        visited[now] = True
        for j in graph[now]:
            cost = distance[j[0]]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])