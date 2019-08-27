import sys
sys.stdin = open('ladder.txt')
def safety(y,x):#벽마주침 방지, 래더의 길(road)이 1(True) 인게 매칭될 때
    return 0 <= y < 100 and 0 <= x < 100 and Ladder[y][x] == 1
def DFS(y,x): #DFS 탐색으로 백트랙킹 방지
    global result
    visited.append((y,x)) #올바른 길 확인된 것 저장
    if y == 0:
        result = x
        return
    for ddd in range(3):#2차원배열 초기화 및 visited 위치 파악 후 저장
        NY = y + dy[ddd]
        NX = x + dx[ddd]
        if safety(NY,NX) and not (NY,NX) in visited:
            return DFS(NY,NX)
for t in range(1, 11): #테스트케이스 만큼 반복되는 for문과 필요 변수 저장
    tc = int(input())
    Ladder = [list(map(int, input().split()))for _ in range(100)]
    st_y = 99
    st_x = Ladder[99].index(2)
    dy = [0,0,-1]
    dx = [-1,1,0]
    result = 0
    visited = []
    DFS(st_y, st_x)
    print('#{} {}'.format(tc, result))

'''
#선생님 풀이
def check(data, x, y):
    if x < 0 or x >= SIZE : return False
    if y < 0 or y >= SIZE : return False
    if data[x][y] == 0 : return False
    if data[x][y] == 9 : return False
    return True
def solve(data):
    x,y,newx,newy = 0, 0, 0, 0
    dx = [0, 0, -1] #왼쪽 오른쪽 위쪾
    dy = [-1, 1, 0]

    for i in range(SIZE):
        if data[SIZE-1][i] == 2:
            x = SIZE - 1
            y = i
            break
    while True:
        if x == 0; return async
        for i in range(3):
            newx = x +dx[i]
            newy = y +dy[i]
            if check(data, newx, newy):
                x = newx
                y = newy
                data[x][y] = 9
                break

T = 10
SIZE = 100
for tc in range(T):
    no = int(input())
    data = [[0for _ in range(SIZE)]for _ in range(SIZE)]
'''