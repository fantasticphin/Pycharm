T =int(input())
for tc in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    data = [[0for _ in range(2)] for _ range(N)]
    ans = [0] * 2
    pos = 0
    for i in range(2):
        for j in range(2):
        data[i][j] = temp[ans]
        pos += 1

    spos = 0
    while(spos<N):
        j = 0
        while(j < N):
            if data[spos][0] == data[j][i]:
                break
            j += 1
        if j == N : break
        spos += 1


    pos = 0
    ans[pos] = data[spos][0]
    pos += 1
    ans[pos] = data[spos][1]
    while(1):
        for i in range(N):
            if ans[pos] == data[i][0]:
                pos += 1
                ans[pos] = data[i][0]
                pos += 1
                ans[pos] = data[i][1]
        if pos == 2*N-1:
            break

    print('#{}'.format(tc+1), end=" ")
    for i in ans:
        print(i, end=' ')
    print()