import sys
sys.stdin=open('2048.txt')

for tc in range(1, int(input())+1):
    N,S = input().split()
    N = int(N)
    bd = [list(map(int,input().split()))for _ in range(N)]
    if S == 'left':
        for i in range(N):
            sav = None
            x,y = None, None
            for j in range(N):
                if bd[i][j]:
                    if sav == bd[i][j]:
                        bd[i][j] *= 2
                        bd[x][y] = 0
                        sav = None
                        x,y = None, None
                else:
                    sav = bd[i][j]
                    x,y = i,j
            cnt = 0
            for j in range(N):
                if bd[i][j]:
                    bd[i][cnt] = bd[i][j]
                    cnt += 1
            for j in range(cnt, N):
                bd[i][j] = 0
    elif S == 'right':
        for i in range(N):
            sav = None
            x,y = None, None
            for j in range(N-1, -1, -1):
                if bd[i][j]:
                    if sav == bd[i][j]:
                        bd[i][j] *= 2
                        bd[x][y] = 0
                        sav = None
                        x,y = None, None
                else:
                    sav = bd[i][j]
                    x,y = i,j
        cnt = N-1
        for j in range(N-1, -1, -1):
            if bd[i][j]:
                bd[i][cnt] = bd[i][j]
                cnt -= 1
        for j in range(cnt+1):
            bd[i][j] = 0
    elif S == 'down':
        for i in range(N):
            sav = None
            x,y = None, None
            for j in range(N-1, -1, -1):
                if bd[i][j]:
                    if sav == bd[i][j]:
                        bd[i][j] *= 2
                        bd[x][y] = 0
                        sav = None
                        x,y = None, None
                else:
                    sav = bd[i][j]
                    x,y = i,j
        cnt = N-1
        for j in range(N-1, -1, -1):
            if bd[i][j]:
                bd[i][cnt] = bd[i][j]
                cnt -= 1
        for j in range(cnt, N):
            bd[i][j] = 0
    elif S == 'up':
        for i in range(N):
            sav = None
            x,y = None, None
            for j in range(N):
                if bd[i][j]:
                    if sav == bd[i][j]:
                        bd[i][j] *= 2
                        bd[x][y] = 0
                        sav = None
                        x,y = None, None
                else:
                    sav = bd[i][j]
                    x,y = i,j
        cnt = 0
        for j in range(N):
            if bd[i][j]:
                bd[i][cnt] = bd[i][j]
                cnt += 1
        for j in range(cnt, N):
            bd[i][j] = 0
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(bd[i][j], end=' ')
        print()