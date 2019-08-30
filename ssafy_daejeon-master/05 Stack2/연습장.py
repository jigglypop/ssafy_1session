import pprint

N = 7
v = [[0]*N for _ in range(N)]

Y, X = len(v), len(v[0])
n = 0
for i in range(0,Y+X-1):
    x = 0 if i < X else (i - X + 1)
    y = i if i < X else X - 1
    while x < X and y > 0:
        x += 1
        y -= 1
        n += 1
        print(x,y)
        v[y][x] = n

pprint.pprint(v)



        