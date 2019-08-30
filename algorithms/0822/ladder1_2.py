def DFS(x,y):
    global ans
    if x == 0: 
        ans = y
        return y
    arr[x][y] = 0
    if y - 1 >= 0 and arr[x][y - 1]:
        return DFS(x, y - 1)
    elif y + 1 < 100 and arr[x][y + 1]:
        return DFS(x, y + 1)
    else:
        return DFS(x -1, y)


for tc in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    x = y = 0
    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break
    print(DFS(x,y))