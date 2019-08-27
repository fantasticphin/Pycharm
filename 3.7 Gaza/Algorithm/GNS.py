import sys
sys.stdin = open('GNS.txt')

T = int(input()) #테스트 케이스 번호 받기
for tc in range(1, T+1): #전체 범위 반복 횟수
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"];cnt_base = {"ZRO" : 0, "ONE" : 0, "TWO" : 0, "THR" : 0, "FOR" : 0, "FIV" : 0, "SIX" : 0, "SVN" : 0, "EGT" : 0, "NIN" : 0};ct_lt = list(input().split())
    for x in input().split(): #입력받은 테스트케이스의 부가 횟수에 카운트 준비
        cnt_base[x] += 1 #카운트 베이스 +1
    print('#{}'.format(tc))
    for i in range(10):
        print('{}'.format((nums[i]+ ' ') * cnt_base[nums[i]]), end=" ") #테스트케이스 수 만큼 반복
    print()

# Base = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
# Base2 = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT',9:'NIN'}
#
# for tc in range(1, T+1):
#     tc_lst = list(input().split())
#     Data = list(input().split())
#     N = len(Data)
#
#     for i in range(N):
#         Data[i] = Base[Data[i]]
#
#     Data.sort()
#
#     for j in range(N):
#         Data[j] = Base2[Data[j]]
#
#     print('%s %s'%(tc_lst[0],' '.join(Data)))