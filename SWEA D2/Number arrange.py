for t in range(1, int(input())+1):
    N  = input()
    X = sorted(list(map(int, input().split())))
    a = map(str, X)
    print(f'#{t} ' + ' '.join(a))
