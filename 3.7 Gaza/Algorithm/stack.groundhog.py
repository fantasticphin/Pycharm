import sys
sys.stdin = open('두더지굴.txt')

#탐색 가능 동굴
def is_wall(x, y):
    global N
    if x < 0 or x >= N:
        return False
    elif y < 0 or y >= N:
        return False
    elif burrow[x][y] == 0:
        return False
    return True

# 동굴 탐색하는 함수
def inspect_burrow(x, y):
    burrow_length = 0  # 동굴 크기 측정 #방향 모를 때 쓰는 함수
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = []

    # burrow[x][y] = 0  # 초깃값 visited check
    # burrow_length += 1  # 동굴 크기 +1
    stack.append([x, y])

    while len(stack) != 0:
        x, y = stack.pop()
        burrow[x][y] = 0
        burrow_length += 1

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if is_wall(tx, ty):
                stack.append([tx, ty])

    return burrow_length



N = int(input())  # 가로 x 세로 크기
burrow = [list(map(int, input().split())) for i in range(N)]

burrow_cnt = 0  # 동굴 갯수 카운트
burrows = []
for i in range(N):
    for j in range(N):
        if burrow[i][j] != 0:
            burrows.append(inspect_burrow(i, j))
            burrow_cnt += 1

print(burrow_cnt)
print(burrows)