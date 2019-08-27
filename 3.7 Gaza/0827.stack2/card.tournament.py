import sys
sys.stdin = open('card.tournament.txt')

def winner_winner_chicken_dinner(a,b): #우승자를 배출하는 함수
    if a[0] - b[0] == 1 or a[0] - b[0] == -2:
        return a
    elif a[0] - b[0] == -1 or a[0] - b[0] == 2:
        return b
    else:
        return a

def party(lisborn): #partition 함수를 통해 피봇 포인트 확보
    if len(lisborn) == 2:
        return winner_winner_chicken_dinner(lisborn[0], lisborn[1])
    elif len(lisborn) == 1:
        return lisborn[0]
    else:
        if len(lisborn)%2 == 1:
            pvt = len(lisborn)//2 #피봇 포인트 (중간값을 조정 후 확보)
        else:
            pvt = (len(lisborn)-1)//2
    apt = party(lisborn[0:pvt+1])
    bpt = party(lisborn[pvt+1:len(lisborn)])
    return winner_winner_chicken_dinner(apt,bpt)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    lisborn = [[data[i], i+1] for i in range(N)]
    rst = party(lisborn)
    print('#{} {}'.format(tc, rst[1]))
