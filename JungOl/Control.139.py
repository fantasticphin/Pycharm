N,M = map(int,input().split())

if N >= M:
    for x in range(1,10):
        for y in range(N,M-1, -1):
            print('{} * {} = {:2}'.format(y,x,x*y), end='   ')
        print()
if N < M:
    for x in range(1,10):
        for y in range(N,M+1):
            print('{} * {} = {:2}'.format(y,x,x*y), end='   ')
        print()