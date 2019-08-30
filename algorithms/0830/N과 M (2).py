def perm(N, n):
    arr = [i for i in range(1,N+1)]
    used = [0 for _ in range(len(arr))]
    def generate(chosen,used):
        if len(chosen) == n:
            chosen = map(str,chosen)
            print(' '.join(chosen))            
            return 
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen,used)
                chosen.pop()
                used[i] = 0
    generate([],used)

N,n = map(int,input().split())
perm(N, n)