import sys
sys.stdin = open('farm_crop.txt')

T = int(input())
for tc in range(1, T+1):
    field = int(input())
    data = [[0 for i in range(field)]for j in range(field)]