from sys import stdin

a, b = map(int, stdin.readline().split())
q = [[0 for i in range(a+1)]] + [([0] + list(map(int, stdin.readline().split()))) for j in range(a)]
dp = [[0 for i in range(a+1)]] + [([0] + [-1 for i in range(a)]) for j in range(a)]

for i in range(b):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    if dp[x2][y2] == -1:
        for j in range(1, x2+1):
            for k in range(1, y2+1):
                dp[j][k] = dp[j-1][k] + dp[j][k-1] - dp[j-1][k-1] + q[j][k]
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])