import sys
sys.stdin = open('maze_swea_algorithm.txt')

def ddffss(x,y):
    vis[x][y] = 1

    if dm[x][y] == '3':
        result[0] = 1
        return
    for dddd in range(4):
        NX = x + dx[dddd]
        NY = y + dy[dddd]
        if dm[NX][NY] != '1' and vis[NX][NY] == 0:
            ddffss(NX, NY)

T = 10
for tc in range(1, T+1):
    N = int(input())
    dm = [[1 for _ in range(18)]for _ in range(18)]
    data = [list(input())for _ in range(16)]

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    result = [0]
    vis = [[0 for _ in range(18)]for _ in range(18)]
    for i in range(1, 17):
        for j in range(1, 17):
            dm[i][j] = data[i-1][j-1]

    for jx in range(1, 17):
        for js in range(1, 17):
            if dm[jx][js]=='2':
                ddffss(jx, js)

    print('#{} {}'.format(tc, result[0]))
    # print(data)
