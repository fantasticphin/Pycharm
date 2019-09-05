import sys
sys.stdin = open('Sudo.txt')

def sudoku():
    for i in range(0, N - 2, 3):
        for j in range(0, N - 2, 3):
            su = set()
            for x in range(3):
                for y in range(3):
                    su.add(sudo[i + x][j + y])
            if len(su) != 9:
                return 0

    for s in range(N):
        su1 = set()
        su = set()
        for v in range(N):
            su.add(sudo[s][v])
            su1.add(sudo[v][s])
        if len(su) != 9 or len(su1) != 9:
            return 0
    return 1

for tc in range(1, int(input())+1):
    N = 9
    sudo = [list(map(int,input().split())) for _ in range(N)]
    su = 1
    if su:
        su = sudoku()
    print('#{} {}'.format(tc, su))

