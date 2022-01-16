from sys import stdin

a = "0"+stdin.readline().rstrip()
b = "0"+stdin.readline().rstrip()
dp = [[-1 for i in range(len(b))] for i in range(len(a))]


def LCS():
    for i in range(len(a)):
        dp[i][0] = 0
    for i in range(len(b)):
        dp[0][i] = 0
    for i in range(1,len(a)):
        for j in range(1,len(b)):
            if a[i] == b[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len(a)-1][len(b)-1]

print(LCS())
