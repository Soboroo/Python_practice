from sys import stdin
input=stdin.readline
print('\n'.join(sorted(sorted(list({input().rstrip()for _ in range(int(input()))})),key=lambda x:len(x))))
