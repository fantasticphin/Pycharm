N,M = map(int,input().split())
for i in range(1, N+1):
    for j in range(1, M+1):
        print(j*i, end =' ')
    print()