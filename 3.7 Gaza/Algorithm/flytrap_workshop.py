import sys
sys.stdin = open('flytrap.txt')

for tc in range(1, int(input())+1):
    N,M = map(int,input().split())
    BOX = [list(map(int,input().split()))for _ in range(N)]
    TRAP = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            TMP = 0
            for i in range(M):
                for j in range(M):
                    TMP += BOX[x+i][y +j]
            if TMP > TRAP:
                TRAP = TMP
    print('#{} {}'.format(tc, TRAP))