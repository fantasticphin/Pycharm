for t in range(int(input())):
    n = input()
    b = int(n)
    z = set()
    while True:
        for L in n:
            z.add(L)
        if len(z) == 10:
            break
        n = str(int(n) + b)
    print('#{} {}'.format(t+1, n))