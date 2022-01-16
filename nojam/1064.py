# pa = list(map(int, input().split()))
# pa = [(pa.pop(), pa.pop()) for _ in range(3)]
#
# if (pa[0][1] - pa[1][1]) * (pa[0][0] - pa[2][0]) == (pa[0][1] - pa[2][1]) * (pa[0][0] - pa[1][0]):
#     print(-1.0)
#     exit()
# length = []
# for i in range(3):
#     length.append(((pa[i][0] - pa[(i + 1) % 3][0]) ** 2 + (pa[i][1] - pa[(i + 1) % 3][1]) ** 2) ** 0.5)
# length.sort()
# print((length[2] * 2 + length[1] * 2) - (length[0] * 2 + length[1] * 2))

from math import dist as x
a,b,c,d,e,f=map(int,input().split())
y=sorted([x((a,b),(c,d)),x((c,d),(e,f)),x((e,f),(a,b))])
print(-1if(b-d)*(a-e)==(b-f)*(a-c)else(y[2]*2+y[1]*2)-(y[0]*2+y[1]*2))

# from math import dist
# import numpy as np
# a = np.array(list(map(int, input().split()))).reshape(-1, 2)
# a.tolist()
# if (a[1][1] - a[2][1]) * (a[0][0] - a[2][0]) == (a[1][1] - a[2][1]) * (a[0][0] - a[1][0]):
#     print(-1.0)
#     exit()
# length = sorted([dist(a[0], a[1]), dist(a[1], a[2]), dist(a[2], a[0])])
# print((length[2] * 2 + length[1] * 2) - (length[0] * 2 + length[1] * 2))

# from math import dist
# pa = list(map(int, input().split()))
# pa = [(pa[i], pa[i+1]) for i in range(0, 6, 2)]
# if (b - d) * (a - e) == (b - f) * (a - c):
#     print(-1.0)
#     exit()
# length = sorted([dist(pa[0], pa[1]), dist(pa[1], pa[2]), dist(pa[2], pa[0])])
# print((length[2] * 2 + length[1] * 2) - (length[0] * 2 + length[1] * 2))