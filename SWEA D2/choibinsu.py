for t in range(int(input())):
    n = input()
    n = list(map(int, input().split()))
    m = 0
    k = 0
    for x in set(n):
        if n.count(x) > m:
            m = n.count(x)
            k = x
    print(f'#{t+1} {k}')