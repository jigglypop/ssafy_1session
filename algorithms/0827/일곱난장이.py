import sys

def D(k,N):
    global R
    if k == N:
        if sum(bits)==7:
            a = bits[::]
            R.append(a)
        return
    bits[k] = 1
    D(k+1,N)
    bits[k] = 0
    D(k+1,N)

sys.stdin = open('input5.txt','r')
m = [int(input()) for _ in range(9)]
m.sort()
N = len(m)
bits = [0] * N
R = []
D(0,N)

for r in R:
    b = []
    for i in range(len(r)):
        if r[i]:
            b.append(m[i])    
    if sum(b) == 100:
        break
for i in b:
    print(i)


