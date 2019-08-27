import sys
sys.stdin = open('두더지굴.txt')

def is_wall(x,y):
    global N
    if x < 0 or x >= N:
        return False
    elif y < 0 or y >= N:
        return False
    elif burrow[x][y] == 0:
        return False
    return True

def burrow_insp(x,y, burrow_length = 0):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = []
    stack.append([x,y])
    while len(stack) != 0:
        x, y = stack.pop(0)

        burrow[x][y] = 0
        burrow_length += 1

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if is_wall(tx, ty):
                stack.append([tx, ty])

    return burrow_length


N = int(input())
burrow = [list(map(int, input().split())) for i in range(N)]

bur_cnt = 0
burrows = []
for i in range(N):
    for j in range(N):
        if burrow[i][j] != 0:
            burrows.append(burrow_insp(i,j))
            bur_cnt += 1

print(bur_cnt)
print(burrows)