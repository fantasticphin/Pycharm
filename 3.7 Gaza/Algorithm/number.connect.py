import sys
sys.stdin = open('number.connect.txt')

dx, dy = [1,-1,0,0], [0,0,1,-1]
def dfs(i,j,t,q):
    if q == 7:
        calc.append(t)
        return
    for d in range(4):
        if -1 < i + dx[d] < 4 and -1 < j + dy[d] < 4:
            dfs(i+dx[d], j+dy[d], t+'{}'.format(puzzle[i+dx[d]][j+dy[d]]), q+1)

for tc in range(1, int(input())+1):
    puzzle = [list(map(int, input().split()))for _ in range(4)]
    calc = []
    for i in range(4):
        for j in range(4):
            dfs(i,j,'{}'.format(puzzle[i][j]), 1)
    print('#{} {}'.format(tc, len(set(calc))))