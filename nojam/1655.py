from sys import stdin
import heapq
input = stdin.readline

a=[]
for i in range(int(input())):
    a.append(int(input()))
    heapq.heapify(a)
    heap = list(a)
    result = 0

    for j in range(len(a)//2+len(a)%2):
        result = heapq.heappop(heap)

    print(result)