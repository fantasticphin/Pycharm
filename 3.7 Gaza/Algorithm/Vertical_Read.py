import sys
sys.stdin = open('Vertical_Read.txt')

# for tc in range(1, int(input())+1):
#     listo = [input()for _ in range(5)]
#     ML = max([len(i) for i in listo]) #입력 변수 내 최대값 구분
#     D = '' #최종 입력값 받을 변수(스트링 타입)
#     DS = []
#     for i in range(ML): #입력값 중 가장 긴 길이의 리스트를 기준으로 세로 검색
#         for j in range(5): #input 값
#             if len(listo[j]) > i:
#                 DS.append(listo[j][i])
#     D = ''.join(DS)
#     print('#{} {}'.format(tc, D))

for tc in range(1, int(input())+1):
    l = [input()for _ in range(5)]
    ML = max([len(i)for i in l])
    D = ''
    for i in range(ML):
        for j in range(5):
            try:
                D += l[j][i]
            except: #index out of range 예외 처리
                pass
    print('#{} {}'.format(tc, D))