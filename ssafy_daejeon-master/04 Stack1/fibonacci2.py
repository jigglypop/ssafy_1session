
def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


for i in range(1, 11):
    print('fibo({}) = {}'.format(i, fibo(i)))


#--------------------------------------------------

# def fibo(n):

# for i in range(1, 11):
#     print('fibo({}) = {}'.format(i, fibo(i))