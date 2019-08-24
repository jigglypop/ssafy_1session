p = 'abcdabcef'   
# pattern 
t = 'alksdabcdabcflaskjflkabcdjsaflkjasdkdsajfabcdabceflksadjabcdaksfjffsdaf'      
# text

m, n = len(p), len(t)
next = [0] * (m + 1)

# 전처리
next[0] = -1
i, j = 0, -1
while i < m:
    while j >= 0 and p[j] != p[i]:
        j = next[j]
    i, j = i + 1, j + 1
    next[i] = j
print(next) 

