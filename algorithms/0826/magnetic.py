import pprint
import sys

def S(M):
    m = list(M)
    for w in m:
        if len(m) == 0:
            return 0
        elif m[0] == '2':
            m.pop(0)
        elif m[-1] == '1':
            m.pop()
        a = ''.join(m)
    return a.count('12')

#sys.stdin = open('input (23).txt','r')
for tc in range(1,11):
    N = int(input())
    m = [list(input().split()) for _ in range(N)]
    M = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            M[y][x] = m[x][y]

    R = []
    for i in range(N):
        s = ''
        for w in M[i]:
            if w == '0':continue
            s += w
        R.append(s)

    r = 0
    for w in R:
        r += S(w)
    print('#{} {}'.format(tc,r))
