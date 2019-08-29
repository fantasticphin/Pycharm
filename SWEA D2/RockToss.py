for t in range(1, int(input())):
    n = input()
    n = map(int,input())
    n = list(map(abs,n))
    print('#{} {} {}'.format(t+1, min(n), n.count(min(n))))
