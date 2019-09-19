import sys
sys.stdin = open('Docking.txt')

def connect(i,e,cnt):
    global time
    for j in range(i+1, N): #재귀재귀재귀
        if T[j][0] >= e:
            connect(j, T[j][1], cnt+1)
    if cnt > time: #횟수 덧셈
        time = cnt

for tc in range(1,int(input())+1):
    N = int(input())
    T = sorted([list(map(int,input().split()))for _ in range(N)], key =lambda x:x[0])    #sorted를 구분하는 기준이 x[0]
    # print(T)
    # print(T) 람다 x[0] key 값
    time = 0
    for i in range(N):
        connect(i, T[i][1], 1)
    print('#{} {}'.format(tc, time))