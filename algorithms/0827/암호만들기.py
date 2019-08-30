import sys
import pprint

def D(k,N):
    global R
    if k == N:
        if sum(bits)==L:
            a = bits[::]
            R.append(a)
        return
    bits[k] = 1
    D(k+1,N)
    bits[k] = 0
    D(k+1,N)
    
#sys.stdin = open('input4.txt','r')
L,C = map(int,input().split())
m = sorted(input().split())
m.sort()

N = len(m)
bits = [0] * C
R = []
D(0,C)
W = []
for w in R:
    s = ''
    for i in range(C):
        if w[i]:
            s += m[i]
    W.append(s)

V = 'aeiou'
for v in W:
    c = 0
    for i in v:       
        if i in V:
            c += 1
    cc = L - c
    if cc >= 2 and c >= 1:
        print(v)


