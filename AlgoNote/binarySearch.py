from sys import stdin


def f(array, key, start, end):
    if start == end:
        if array[start] == key:
            return 1
        else:
            return 0
    middle = (start + end) // 2
    if key <= array[middle]:
        return f(array, key, start, middle)
    else:
        return f(array, key, middle + 1, end)


a = int(input())
n = sorted(list(map(int, stdin.readline().split())))
b = input()
for i in list(map(int, stdin.readline().split())):
    print(f(n, i, 0, a - 1), end=' ')
