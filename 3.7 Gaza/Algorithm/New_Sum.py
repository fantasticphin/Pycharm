import sys
sys.stdin=open('New_Sum.txt')

for tc in range(1, int(input())+1):
    p,q = map(int,input().split())
    n = 0
    a = 0
    tmps = 0
    while p > a:
        n += 1
        a = (n*(n+1)//2)
    tmps = a - p
    nx = n -tmps
    ny = 1 + tmps
    n = 0
    a = 0
    while q > a:
        n += 1
        a = (n*(n+1)//2)
    tmps = a - q
    nxx = n - tmps
    nyy = 1 + tmps
    coordinates = (nx + nxx, ny + nyy)
    sol2 = coordinates[1] - 1
    print('#{} {}'.format(tc, sol2))