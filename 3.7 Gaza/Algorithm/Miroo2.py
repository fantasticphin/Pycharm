import sys
sys.stdin = open('Miroo.txt')

for t in range(1, 11):
    input()
    n = 100
    mz = [list(map(int, input()))for _ in range(n)]

    stk = [(1,1)]
    ans = 0
    i,j = 1,1
    while stk:
        if mz[i][j] == 3:
            ans = 1
            break

        mz[i][j] = 1
        dir = [1,-1,1,-1]
        for x in dir[:2]:
            if i+x < n-2 and i+x > 0:
                if mz[i + x][j] != 1:
                    stk.append((i+x, j))
        for y in dir[2:]:
            if j+y < n-2 and j+y > 0:
                if mz[i][j+y] != 1:
                    stk.append((i, j+y))
        if len(stk) > 0:
            d = stk.pop()
        else:
            ans = 0
            continue
        i,j = d[0], d[1]
    print('#{} {}'.format(t, ans))