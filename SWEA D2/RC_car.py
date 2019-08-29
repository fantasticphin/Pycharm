for t in range(int(input())):
    n = int(input())
    v = 0 #속도
    d = 0 #거리
    for i in range(n):
        C = list(map(int,input().split()))
        if C[0] == 1:
            v += C[1]
        elif C[0] == 2:
            if v - C[1] >= 0:
                v -= C[1]
            else: v = 0
        else:
            v = v
        d += v
    print('#{} {}'.format(t+1, d))