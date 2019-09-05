import sys
sys.stdin = open('Array_Spin.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    S = [''.join(input().split())for i in range(N)]#원본 배열
    # print(S)
    Sr = S[::-1] #배열 역순
    # print(Sr)
    S90 = [''.join(j) for j in list(zip(*Sr))]#90도 회전 보기
    # print(S90)
    S90r = S90[::-1] #정렬
    # print(S90r)
    S180 = [''.join(j) for j in list(zip(*S90r))] #180도 회전 보기
    # print(S180)
    S180r = S180[::-1] #정렬
    S270 = [''.join(j) for j in list(zip(*S180r))] #270도 회전 보기
    # print(S270)
    S270r = S270[::-1] # 정렬
    print('#{}'.format(tc))
    for x in range(N):
        print('{} {} {}'.format(S90[x], S180[x], S270[x])) #정렬된 최종 배열 순차적 배회