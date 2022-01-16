from sys import stdin
from queue import PriorityQueue

for i in range(int(input())):
    que = PriorityQueue(maxsize=int(input()))
    result = 0
    for j in map(int, stdin.readline().split()):
        que.put(j)
    while que.qsize() > 1:
        tmp = que.get() + que.get()
        result += tmp
        que.put(tmp)
    print(result)