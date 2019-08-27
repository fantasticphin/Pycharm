import sys
sys.stdin = open("구간합.txt")

T = int(input())

for tc in range(1, T+1):
    M , N = map(int,input().split())
    li = list(map(int,input().split()))
    la = []
    for x in range(len(li) - N + 1):
        a = 0
        for y in range(N):
            a += li[x + y]
        la.append(a)
    c = max(la) - min(la)
    print('#{} {}'.format(tc, c))