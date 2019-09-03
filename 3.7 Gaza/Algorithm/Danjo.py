import sys
sys.stdin = open('Danjo.txt')

def CHECKER(x):
    for i in range(len(x)-1):
        if x[i+1] < x[i]:
            return False
    return True

for tc in range(1, int(input())+1):
    X = int(input())
    NL = list(map(int,input().split()))
    check = -1 #단조 아닐 시 출력
    for i in range(1, X - 1):
        for j in range(i + 1, X):
            x = NL[i] * NL[j]
            if x > check: #체커 발동 조건
                if CHECKER(str(x)): #체커가 참일시
                    check = x #x 변수에 체커 값 기입
    print('#{} {}'.format(tc, check))