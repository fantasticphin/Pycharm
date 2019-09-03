import sys
sys.stdin = open('Orthello.txt')

def orthell(x,y,p):
    x -= 1
    y -= 1
    b[x][y] = p
    add = [False]*8
    a = [0]*8

    for zz in range(8):
        for i in range(1,N):
            tx = x+dx[zz] * i
            ty = y +dy[zz] * i
            if 0 <= tx < N and 0<= ty < N:
                if b[tx][ty] == 0:
                    break
                elif b[tx][ty] == p:
                    add[zz] = True
                    break
                else:
                    a[zz] += 1
            else:
                break

    for zz in range(8):
        if add[zz]:
            for i in range(1, a[zz]+1):
                tx = x + dx[zz] * i
                ty = y + dy[zz] * i
                b[tx][ty] = p

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]
for tc in range(1, int(input())+1):
    N,M = map(int,input().split())
    b = [[0]*N for _ in range(N)]
    b[N//2][N//2], b[N//2-1][N//2-1] = 2,2
    b[N//2-1][N//2], b[N//2][N//2-1] = 1,1
    for _ in range(M):
        a = list(map(int,input().split()))
        orthell(*a)
    bb, ww = 0,0
    for i in range(N):
        for j in range(N):
            if b[i][j] == 1:
                bb += 1
            elif b[i][j] == 2:
                ww += 1
    print('#{} {} {}'.format(tc, bb, ww))