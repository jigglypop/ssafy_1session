# 4장 연습문제2

def check_paren(exp):
    stack = []

    for ch in exp:
        if ch == '(':
            stack.append(ch)
        else:
            if len(stack) != 0:
                stack.pop()        # 스택에 있으면 pop
            else:
                return False
    if len(stack) > 0:     # 스택에 다 거치고 남은게 있으면 False
        return False
    return True    # 다 아니면 True

str1 = '()()((()))'
str2 = '((()((((()()((()())((()))))'
print(check_paren(str1))
print(check_paren(str2)) 
# if check_paren(str2):
#     print('OK')
# else:
#     print('FAIL')

