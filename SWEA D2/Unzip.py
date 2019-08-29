for t in range(int(input())):
    n = int(input())
    Q = ' '
    for _ in range(n):
        a,b = input().split()
        Q += a * int(b)
    print('#{}'.format(t+1))
    for i in range(len(Q)//10):
        print(Q[10*i:10*(i+1)])
    if len(Q)%10:
        print(Q[10 * (len(Q) // 10):])