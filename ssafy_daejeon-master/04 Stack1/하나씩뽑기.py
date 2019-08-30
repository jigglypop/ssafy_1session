def D(a,n):
    global c
    if a[0] == n:
        return c
    a.pop(0)
    c += 1
    return D(a,n)
a = [1,5,4,3,2,7,8,6]
b = a[:]
r = []
c = 0
for i in range(1,9):
    D(a,i)
    r.append(c)
    c = 0
    a = b[:]
print(r)
