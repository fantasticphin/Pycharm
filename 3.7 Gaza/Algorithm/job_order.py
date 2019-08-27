import sys
sys.stdin = open('job_order.txt')

for tc in range(1, 11):
    v,e = map(int,input().split())
    mp = [[0]*(v+1) for _ in range(v + 1)]
    vs = []

    dt = list(map(int, input().split()))
    N = int(len(dt)/2)

    for i in range(N):
        r = dt[i*2]
        c = dt[i*2+1]
        mp[c][r] = 1

    result = []
    while True:
        if len(result) == v:
            break

        st_c = []
        for c in range(1, len(mp)):
            if 1 not in mp[c] and c not in result:
                st_c.append(c)
        #print(st_c)

        for c in st_c:
            result.append(c)
            for r in range(len(mp)):
                mp[r][c] = 0
        #print(mp)

    print('#{}'.format(tc), end=" ")
    for i in result:
        print('{}'.format(i), end=" ")
    print()
