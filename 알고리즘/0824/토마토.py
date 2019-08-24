import pprint
from collections import deque
import sys

def BFS(Q):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    while Q:
        w = Q.popleft()
        for i in range(4):
            ny = w[0] + dy[i]
            nx = w[1] + dx[i]
            if m[ny][nx] !=-1 and 0 <= ny < N and 0 <= nx < M:
                m[ny][nx] = 1
                Q.append([ny,nx]) 
            


sys.stdin = open('input6.txt','r')
M,N = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(N)]
pprint.pprint(m)

q = []
for y in range(N):
    for x in range(M):
        if m[y][x] == 1:
            q.append([y,x])
print(q)
Q = deque(q)
print(Q)

