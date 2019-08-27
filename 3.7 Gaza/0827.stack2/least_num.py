import sys
sys.stdin = open('least_num.txt')

def cal(y):
    global s_res, res

    if res < s_res:
        return

    if y == N:
        if s_res < res:
            res = s_res
        return

    for visc in range(N):
        if not vs[visc]:
            vs[visc] = True
            s_res += lt[y][visc]
            cal(y+1)
            vs[visc] = False
            s_res -= lt[y][visc]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lt = [list(map(int, input().split())) for _ in range(N)]
    vs = [0]*N
    s_res, res = 0, 987654321
    cal(0)

    print('#{} {}'.format(tc, res))