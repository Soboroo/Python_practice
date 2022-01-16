mod = 1000000007


def pow2(a, x):
    if x == 0:
        return 1
    if x % 2 == 0:
        return pow2(a, x // 2) ** 2 % mod
    else:
        return a * pow2(a, x - 1) % mod


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1) % mod


def binom(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    ans = 0
    for i in range((n - 1) // 2 + 1):
        ans += pow2(2, i) * binom(n - 2 * i, i)

    return ans % mod


print(fibonacci(int(input())))
