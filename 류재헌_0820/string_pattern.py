import sys
sys.stdin = open('string_pattern.txt')

# def pattern(strs_1, strs_2):
#     cnt = 0
#     for i in strs_2:
#         for x in range(strs_2 - strs_1+1):
#             if i[x : x + 4] == strs1[:]:
#                 cnt += 1
#     return cnt
#
# T = int(input())
# for tc in range(1, T+1):
#     a = input().split()
#     b = input().split()
#     print('#{} {}'.format(tc, pattern(a,b)))

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 0
    for j in range(len(str2)-len(str1) + 1):
        cnt = 0
        if(str1[0] == str2[j]):
            cnt += 1
            for k in range(1, len(str1)):
                if str1[k] == str2[j+k]:
                    cnt += 1
                if(cnt == len(str1)):
                    result = 1
                    break
    print("#%d %d" % (tc, result))