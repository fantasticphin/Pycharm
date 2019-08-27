import sys
sys.stdin = open("전기버스.txt")

T = int(input())

for tc in range(1, T + 1):
    N, M, O = map(int,input().split())
    bs = list(map(int, input().split()))
    bst = 0
    chrg = 0
    bs.append(M)

    for j in range(O+1):
        for i in range(N, 0, -1):
            if bst + i in bs:
                bst = bst + i
                chrg += 1
                break
    if bst == M:
        print('#{} {}'.format(tc, chrg -1))
    else:
        print('#{} 0'.format(tc))