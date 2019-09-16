import sys
sys.stdin = open('Binary_2.txt')

def checking(N):
    dec = ''
    while int(N) != N:
        N *= 2
        if N >= 1:
            dec += '1'
            N -= 1
        else:
            dec += '0'
            if len(dec) >= 13:
                dec = 'overflow'
                return dec
    return dec

for tc in range(1, int(input())+1):
    N = float(input())
    checking(N)
    # NN = int(N)
    # print(N, NN)
    print('#{} {}'.format(tc, checking(N)))