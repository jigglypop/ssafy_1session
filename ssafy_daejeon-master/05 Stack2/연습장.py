def exp(x,n):
    if n <= 1:
        return x**n
    if n & 1:
        return exp(x,(n-1)//2) * exp(x,(n-1)//2) * x
    else:
        return exp(x,n//2) ** 2

print(exp(10,0))
print(exp(10,1))
print(exp(10,10))
print(exp(10,9))