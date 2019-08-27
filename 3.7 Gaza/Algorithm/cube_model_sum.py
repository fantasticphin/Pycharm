import sys
sys.stdin = open ("cube_model.txt")

T = 10

for tc in range(1, T+1):
    st = int(input())
    # tcr = list(map(int,input().split()))

    data = [list(map(int, input().split())) for _ in range(100)]
    tot_max = 0

    # print(data)

    for i in range(len(data)): #행과 열의 숫자 합산
        sum_x = 0
        sum_y = 0
        for j in range(len(data[i])):
            sum_x += data[i][j]
            sum_y += data[j][i]
        if sum_x > tot_max: #행과 열의 숫자 총 합산
            tot_max = sum_x
        if sum_y > tot_max:
            tot_max = sum_y
        # print(sum_x, sum_y)

    for i2 in range(len(data)): #좌측상단에서 우측하단 대각선 숫자 합산
        sum_dx = 0
        sum_dy = 0
        for ix in range(len(data[i2])):
            sum_dx = data[i2][ix]
            sum_dy = data[ix][i2]
        if sum_dx > tot_max: #좌측상단에서 우측하단 대각선 숫자 총합산
            tot_max = sum_dx
        if sum_dy > tot_max:
            tot_max = sum_dy

        # print(sum_dx, sum_dy)

    for i3 in range(len(data)): #우측상단에서 좌측하단 대각선 숫자 합산
        sum_ndx = 0
        sum_ndy = 0
        for ixs in range(len(data)):
            sum_ndx = data[ixs][i3]
            sum_ndy = data[i3][ixs]
        if sum_ndx > tot_max: #우측상단에서 좌측하단 대각선 숫자 총합산
            tot_max = sum_ndx
        if sum_ndy > tot_max:
            tot_max = sum_ndy
        # print(sum_ndx, sum_ndy)

    print('#{} {}'.format(tc, tot_max))

    #강사님 풀의
    for tc in range(T):
        no = int(input())
        data = [[ 0 for _ in range(100)]for _ in range(100)]
        for i in range(100):
            data[i] = list(map(int,input().split()))
    # data = [list(map(int,input().split()))for _ in range(100)]
