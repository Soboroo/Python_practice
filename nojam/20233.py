a = [int(input()) for i in range(4)]
n = int(input())
print(max((n-30)*a[1]*21, 0)+a[0], max((n-45)*a[3]*21, 0)+a[2])