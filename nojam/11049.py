from sys import stdin
n = int(input())
dp = [[0 for i in range(n)] for j in range(n)]
matrix = []
a, b = 0, 0
for i in range(n):
    a, b = map(int, stdin.readline().split())
    matrix.append(a)
matrix.append(b)


def matrixChain(i, j):
    if i == j:
        return 0
    if dp[i][j] != 0:
        return dp[i][j]
    dp[i][j] = float('inf')
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], matrix[i-1] * matrix[k] * matrix[j] + matrixChain(i, k) + matrixChain(k + 1, j))
    return dp[i][j]


print(matrixChain(0, n - 1))  # 최소 곱셈 횟수
