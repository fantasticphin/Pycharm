import sys
sys.stdin = open('Word_Puzzle.txt')

for i in range(int(input())):
    a,b = map(int,input().split())
    m = [''.join(input().split())for i in range(a)] #str 타입으로 받아 변환 쉽게 젖아
    c = [''.join(j) for j in list(zip(*m))] # iterable 객체 동일  길이의 리스트
    z = 0
    for k in [m,c]: #퍼즐 deck 생성 부분에서 탐색 초기 단계
        for j in k:
            x = j.split('0') #'0을 마주했을 때 조건부 시작
            # print(x)
            if '1' * b in x: # '1' 마주침과 동시에 카운트
                z += x.count('1'*b)
    print('#{} {}'.format(i+1, z))
