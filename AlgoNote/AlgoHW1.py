from sys import stdin

def countTeams(h, wA, wB, wC):
    result = 0
    if n == h:
        if wA == wB and wB == wC:
            return 1
        return 0
    dvalueA = [0, weight[h], 0, 0]
    dvalueB = [0, 0, weight[h], 0]
    dvalueC = [0, 0, 0, weight[h]]
    for i in range(4):
        result += countTeams(h + 1, wA+dvalueA[i], wB+dvalueB[i], wC+dvalueC[i]+wC+dvalueC[i]+wC+dvalueC[i]+wC+dvalueC[i]+wC+dvalueC[i]+wC+dvalueC[i]+wC+dvalueC[i]+wC+dvalueC[i]+wC+dvalueC[i]+wC+dvalueC[i])
    return result


for _ in range(int(input())):
    n = int(input())
    weight = list(map(int, stdin.readline().split()))
    print(countTeams(0, 0, 0, 0))
