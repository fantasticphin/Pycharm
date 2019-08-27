import sys
sys.stdin = open('calculator.stack2.txt')

T = int(input())
for tc in range(1, T + 1):
    data = list(input().split())
    N = len(data)
    stk = []
    flag = 0
    for i in range(N - 1):
        if data[i].isdigit():
            stk.append(data[i])
    # print(stk)
        else:
            try:
                nums1, nums2 = int(stk.pop()), int(stk.pop())
                if data[i] == '+':
                    result = nums1 + nums2
                elif data[i] == '-':
                    result = nums1 - nums2
                elif data[i] == '/':
                    result = nums2 // nums1
                elif data[i] == '*':
                    result = nums1 * nums2

                stk.append(str(result))

            except:
                flag = 987654321

    if flag == 0 and len(stk) == 1:
        print('#{} {}'.format(tc, stk[0]))
    elif flag == 987654321 or len(stk) != 0:
        print('#{} error'.format(tc))