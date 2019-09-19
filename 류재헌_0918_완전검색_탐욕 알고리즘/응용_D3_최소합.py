import sys
sys.stdin=open('min_addition.txt')
def checks(a,b,c):
    global ans
    if c > ans:
        return
    if a == N-1 and b == N-1:
        if c < ans:
            ans = c
        return

    for i in range(2):
        tx = a + xx[i]
        ty = b + yy[i]

        if -1 < tx < N and -1 < ty < N:
            checks(tx, ty, c + checker[ty][tx])

xx = [1,0]
yy = [0,1]
for tc in range(1, int(input())+1):
    N = int(input())
    checker = [list(map(int,input().split()))for _ in range(N)]
    ans = 9987654321
    c = checker[0][0]
    checks(0,0,c)
    print('#{} {}'.format(tc, ans))
