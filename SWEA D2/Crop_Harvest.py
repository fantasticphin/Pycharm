import sys
sys.stdin = open('Crop_Harvest.txt')

for tc in range(1,int(input())+1):
    N = int(input())
    FIELD = [input()for _ in range(N)]
    s = sum([int(i) for i in FIELD[N//2]]) #농작물 수확할 중앙값 구하기
    # print(s)
    N //= 2
    for i in range(N): #필드 기준 분할
        s += int(FIELD[i][N])
        s += int(FIELD[-i-1][N])
        for j in range(i): #필드 row 별 검색
            s += int(FIELD[i][N+j+1])
            # print(s)
            s += int(FIELD[i][N-j-1])
            # print(s)
            s += int(FIELD[-i-1][N+j+1])
            # print(s)
            s += int(FIELD[-i-1][N-j-1])
            # print(s)
    print('#{} {}'.format(tc, s))