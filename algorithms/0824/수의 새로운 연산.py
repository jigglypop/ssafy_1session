import pprint
import sys

sys.stdin = open('input (3).txt','r')
T = int(input())
for tc in range(1,T+1):
    p, q = map(int,input().split())
    N = 301
    v = [[0]*N for _ in range(N)]
    Y, X = len(v), len(v[0])
    n = 0
    for diag in range(0,Y+X-1):
        x = 0 if diag < X else diag-X+1
        y = diag if diag < X else X-1
        while x < N and y >= 0:
            n += 1
            v[y][x] = n
            y -= 1
            x += 1
    r = []
    for y in range(N):
        for x in range(N):
            if v[y][x] == p:
                r.append([y,x])
    for y in range(N):
        for x in range(N):
            if v[y][x] == q:
                r.append([y,x])
    print(f'#{tc} {v[r[0][0] + r[1][0] + 1][r[0][1] + r[1][1] + 1]}')

