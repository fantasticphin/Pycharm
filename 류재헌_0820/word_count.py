import sys
sys.stdin = open('word_count.txt')

T = int(input())

for tc in range(1, T+1):
    st_1 = list(set(input())) #중복제거 작업 => set
    st_2 = list(input()) # 리스트 생성
    maxescnt = 0
    for i in range(len(st_1)):
        cnt = 0
        for j in range(len(st_2)):
            if (st_1[i] == st_2[j]):
                cnt += 1
            if (cnt > maxescnt):
                maxescnt = cnt
    print('#{} {}'.format(tc, maxescnt))