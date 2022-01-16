def hanoi(a, b, c, n):
    if n == 1:
        print(a, b)
        return
    hanoi(a, c, b, n - 1)
    print(a, b)
    hanoi(c, b, a, n - 1)
    return


n = int(input())
print(2 ** n - 1)
hanoi(1, 3, 2, n)
