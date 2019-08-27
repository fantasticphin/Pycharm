import sys
sys.stdin = open("special.txt")


def gyoyeols(mini_gyo):
    for x in range(len(mini_gyo) - 1):
        m = x
        for y in range(x+1, len(mini_gyo)):
            if x % 2 == 0:
                if mini_gyo[m] < mini_gyo[y]:
                    m = y
            else:
                if mini_gyo[m] > mini_gyo[y]:
                    m = y
        mini_gyo[m], mini_gyo[x] = mini_gyo[x], mini_gyo[m]

T = int(input())

for tc in range(1, T+1):
    itsx = int(input())
    nambas = list(map(int, input().split()))
    gyoyeols(nambas)
    print('#{}'.format(tc), end=" ")
    for i in nambas[0:10]:
        print(i,end=" ")
    print()