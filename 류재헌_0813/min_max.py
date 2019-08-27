import sys
sys.stdin = open("min_max_input.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    aj = list(map(int, input().split()))
    # asj = sorted(aj)
    # maxj = 0
    # minj = 0
    # for i in asj:
    #     maxj = asj[-1]
    #     minj = asj[0]
    #     max_diff = maxj - minj
    # print('#{} {}'.format(test_case, max_diff))
    minj = aj[0]
    maxj = aj[0]
    for x in aj:
        if minj > x:
            minj = x

        if maxj < x:
            maxj = x

    max_diff = maxj - minj
    print('#{} {}'.format(test_case, max_diff))