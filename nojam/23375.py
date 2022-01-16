a, b = map(int, input().split())
r = int(input())
dx = [r, r, -r, -r]
dy = [r, -r, -r, r]
for i in range(4):
    print(a + dx[i], b + dy[i])