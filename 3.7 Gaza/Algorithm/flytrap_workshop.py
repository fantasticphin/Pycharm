import sys
sys.stdin = open('flytrap.txt')


for line in range(int(input())):
    N, M = input().split()
    N = int(N)
    M = int(M)

    MAPS = [list(map(int, input().split())) for nsx in range(N)]
    max_vt = 0
    for nsx in range(N - M + 1):
        for nt2 in range(N - M + 1):
            tmps = 0
            for nos in range(M):
                for nqt in range(M):
                    tmps += MAPS[nsx + nos][nt2 + nqt]
            if max_vt < tmps:
                max_vt = tmps

    print("#{} {}".format(line + 1, max_vt))