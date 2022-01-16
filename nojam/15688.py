from sys import stdin
print('\n'.join(map(str, sorted([int(stdin.readline()) for i in range(int(input()))]))))