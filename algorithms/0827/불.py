import sys
from collections import deque
import pprint

def BFSM(v):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    Q = deque()
    Q.append(v)
    while Q:
        sy,sx = Q.poplift()
        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]

def BFSF(v):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    Q = deque()
    Q.append(v)
    while Q:
        sy,sx = Q.poplift()
        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]

sys.stdin = open('input6.txt','r')
T = int(input())
for _ in range(T):
    w,h = map(int,input().split())
    m = [['$']*(w+2)] + [['$'] + list(input()) + ['$'] for _ in range(h)] + [['$']*(w+2)]
    pprint.pprint(m)
    
    for y in range(h+2):
        for x in range(w+2):
            if m[y][x] == '@':
                v = [y,x] 
    BFS(v)

