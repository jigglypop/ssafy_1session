memo = [0] * 11
memo[1] = 1
for i in range(2, 11):
    memo[i] = memo[i - 1] + memo[i - 2]

for i in range(1, 11):
    print('memo[{}] = {}'.format(i, memo[i]))



# ------------------------------------------------------

# for i in range(1, 11):
#     print('memo[{}] = {}'.format(i, memo[i]))