for i in range(int(input())):
    a = [list(map(int, input().split())) for j in range(int(input()))]
    print(sorted(a))
    print(sorted(a, key=lambda x: x[1]))