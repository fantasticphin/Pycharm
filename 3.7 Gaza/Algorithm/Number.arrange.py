def wall(y,x):
    if y <0 or y>=4:return False
    if x < 0 or x >= 4: return False
    return True

def grid(y,x, cnt):
    for i in range(4):
        ny = y+dy[i]
        nx = x + dx[i]
        if cnt >= 7:
            acc.add(''.join(temp))
            return
        if wall(ny, nx) == True:
            temp.append(data[ny][nx])
            grid(ny, nx, cnt+1)
            temp.pop()

for tc in range(1, int(input())+1):
    data = [input().split() for _ in range(4)]
    temp=[]
    acc= set()
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    for y in range(4):
        for x in range(4):
            grid(y,x,0)

    print('#{} {}'.format(tc, len(acc)))