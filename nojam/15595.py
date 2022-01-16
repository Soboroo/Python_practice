from sys import stdin
input=stdin.readline
n = int(input())
u = dict()
ac = 0
wa = 0
# 맞은 후 제출은 계산하지 않는다.
for i in range(n):
    t = input().split()
    if t[1] != 'megalusion':
        if t[1] not in u: # 처음 등장한 경우
            u[t[1]] = [0, False] # 오답 횟수, 정답 여부
        if u[t[1]][1]: # 정답이면
            continue
        if t[2] == '4':
            u[t[1]][1] = True
            ac += 1
            wa += u[t[1]][0]
        else:
            u[t[1]][0] += 1

print(ac/(ac+wa)*100 if ac else 0)