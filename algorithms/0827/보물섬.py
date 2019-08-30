import sys
from collections import deque
#import pprint


def BFS(M):
    R = []
    for y in range(Y):
        for x in range(X):
            if M[y][x] == 'L':
                Q = deque()
                Q.append((y,x))
                dy = [-1,1,0,0]
                dx = [0,0,-1,1]
                r = 0
                visit = [[0]*X for _ in range(Y)]
                while Q:
                    sy,sx = Q.popleft()                    
                    if visit[sy][sx] > r:
                        r = visit[sy][sx]                    
                    for i in range(4):
                        ny = sy + dy[i]
                        nx = sx + dx[i]
                        if 0 <= ny < Y and 0<= nx < X:
                            if M[ny][nx]=='L' and visit[ny][nx] == 0:
                                visit[ny][nx] += visit[sy][sx] + 1
                                Q.append((ny,nx))
                pprint.pprint(visit)
                R.append(r)
                print(R)
    return max(R)
                  
#sys.stdin = open('input2.txt','r')
Y,X= map(int,input().split()) 
M = [list(sys.stdin.readline().strip()) for _ in range(Y)]

print(BFS(M))
