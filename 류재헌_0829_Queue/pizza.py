import sys
sys.stdin = open('pizza.txt')

for t in range(1, int(input())+1):
    N,M = map(int, input().split())
    Hwadeok = list(map(int, input().split()))
    Piz = []
    for fire in range(1, N+1):
        Piz.append([fire, Hwadeok.pop(0)])
    i = 0
    while len(Piz):
        d = i % N
        Piz[d][1] //= 2
        if not Piz[d][1]:
            if Hwadeok:
                fire += 1
                Piz[d] = [fire, Hwadeok.pop(0)]
            else:
                comps = Piz.pop(d)
                N -= 1
                i = d
                continue
        i += 1
    print('#{} {}'.format(t, comps[0]))
