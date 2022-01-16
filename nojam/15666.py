n, m = map(int, input().split())
a = list(sorted(set(map(int, input().split()))))
result = []


def backtrace(i):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for j in range(i, len(a)):
        result.append(a[j])
        backtrace(j)
        result.pop()


backtrace(0)
