while True:
    a = list(map(int, input().split()))
    if a.count(0) == 3:
        break
    elif len(set(a)) == 1:
        print("Equilateral")
    elif sum(a)/2 <= max(a):
        print("Invalid")
    elif len(set(a)) == 2:
        print("Isosceles")
    else:
        print("Scalene")