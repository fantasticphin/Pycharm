import sys
sys.stdin = open('RowSearch.txt')

def brabus(i,j):
    x = 0
    y = 0
    global N
    while data[i+x][j]:
        x += 1
        if i + x == N:
            break
    while data[i][j+y]:
        y += 1
        if j + y == N:
            break
    for p in range(i, i + x):
        for q in range(j, j + y):
            data[p][q] = 0
    return x, y


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int,input().split()))for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(N):
            if data[i][j]:
                ans.append(brabus(i,j))
    ans.sort()
    ans.sort(key=lambda x: x[0]*x[1])
    print('#{} {}'.format(tc, len(ans)), end=' ')
    for a in ans:
        print('{} {}'.format(a[0], a[1]), end=' ')
    print()