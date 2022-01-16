x, a, b = map(int, input().split(" : "))
x = x * 3600 + a * 60 + b
y, a, b = map(int, input().split(" : "))
y = y * 3600 + a * 60 + b
print((y-x)%86400)