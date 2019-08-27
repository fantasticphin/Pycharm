import sys
sys.stdin = open('2dimension.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(M)]
    # data_xs = [list(map(int, input()))for _ in range(M)]
    # print(data_xs)

    for i in range(M):
        print("{} {}".format(i,data[i]))