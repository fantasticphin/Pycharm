import sys
sys.stdin = open('Container.txt')

for tc in range(1, int(input())+1):
    N,M = map(int,input().split())
    N_wt = sorted(list(map(int,input().split())))
    M_max = sorted(list(map(int,input().split())))
    dap = 0
    route = N -1
    for i in range(M-1, M-min(N,M)-1, -1):
        while True:
            if M_max[i] >= N_wt[route]:
                dap += N_wt[route]
                route -= 1
                break
            else:
                route -= 1
                if route < 0:
                    break
    print('#{} {}'.format(tc, dap))