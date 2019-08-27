import sys
sys.stdin = open("Algo_work_03.txt")
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     scrw = list(map(int, input().split()))
#     scr_matx = []
#     scr_matxs = []
#     ans = []
#     tem = 0
#     jos = 0
#     sc_index = 0
#
#     for i in range(N*2): #짝수 홀수 분류 후 리스트 정렬 삽입
#         if i % 2 == 0:
#             scr_matx.append(scrw[i])
#         else:
#             scr_matxs.append(scrw[i])
#
#     for k in range(len(scr_matx)): #길이 구분 후, 구분별 리스트 미 포함시 동작 구분
#         if scr_matx not in scr_matxs:
#             tem = scr_matx[k]
#             sc_index = k
#             ans = [scr_matx[k]]+[scr_matxs[k]]
#
#     while len(ans) < len(scrw):
#
#         if ans[-1] == scr_matx[jos]:
#             ans += [scr_matx[jos]] + [scr_matxs[jos]]
#             jos = 0
#         else:
#             jos += 1
#
#     print('#{}'.format(tc+1), end=" ")
#     for k in ans:
#         print(k, end=" ")
#     print()
T = int(input())
for tc in range(T):
    cnt = int(input())
    lst1 = list(map(int, input().split()))
    lst2, lst3 = [], []
    ans = []
    s,j = 0, 0
    s_index = 0
    for i in range(cnt*2):
        if i %2 == 0:
            lst2.append(lst1[i])
        else:
            lst3.append(lst1[i])
    for k in range(len(lst2)):
        if lst2[k] not in lst3:
            s = lst2[k]
            s_index = k
            ans = [lst2[k]]+[lst3[k]]
    while len(ans) < len(lst1):
        if ans[-1] == lst2[j]:
            ans += [lst2[j]]+ [lst3[j]]
            j = 0
        else:
            j += 1
    print('#{}'.format(tc+1), end=" ")
    for k in ans:
        print(k, end=" ")
    print()