import sys
sys.stdin = open("multi_list.txt")

T = int(input())

for tc in range(T):
    row, col = map(int, input().split()) #2차원 배열일 때 가로 세로 길이를 준다
    data = [[0 for _ in range(col)] for _ in range(row)]
    data = [list(map(int, input().split())) for _ in range(row)] #방법 1
    print(data)
    # for i in range(row): #방법 2
    #     data[i] = list(map(int, input().split())) #방법 2

    # print(data) #파이썬 방법

    # for i in range(row):
    #     for j in range(col):
    #         print(data[i][j], end=" ")
    #     print()