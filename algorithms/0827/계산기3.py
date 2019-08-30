import sys

sys.stdin = open('input.txt','r')
for tc in range(1, 11):
    n = int(input())
    m = input()
    s = []
    for w in m:
        if w in '123456789':
            s.append(w)
    print(s)                                                                                                                                                                                                                                                                                                                                           