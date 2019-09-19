import sys #순열문제 / TSP
sys.stdin = open('electric_cart.txt')

def energy(a,b,c):
    global check
    if c > check: return

    if a == b:
        c += MAP[A[-1]][0]
        if c < check:
            check = c
    else:
        for i in range(b,a):
            A[b], A[i] = A[i], A[b]
            energy(a,b+1, c+MAP[A[b-1]][A[b]])
            A[b], A[i] = A[i], A[b]


for tc in range(1, int(input())+1):
    N = int(input())
    MAP = [list(map(int,input().split()))for _ in range(N)]
    A = [i for i in range(N)]
    check = 987654321
    energy(N,1,0)

    print('#{} {}'.format(tc, check))
