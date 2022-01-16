from sys import stdin
n = int(input())
dist = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))
sumDist = [0 for i in range(n-1)]
sumDist[0] = dist[0]
currentFuel = 0
result = 0

for i in range(1, n-1):
    sumDist[i] = sumDist[i - 1] + dist[i]

i=0
while i < n-1:
    if currentFuel < sumDist[-1] - (sumDist[i-1] if i != 0 else 0):
        j = i
        while j < n-1 and currentFuel < sumDist[-1] - (sumDist[i-1] if i != 0 else 0):
            if cost[i] <= cost[j]:
                currentFuel += dist[j]
                result += cost[i] * dist[j]
                j += 1
            else:
                currentFuel -= sumDist[j-1] - (sumDist[i-1] if i != 0 else 0)
                i = j
    else:
        break

print(result)