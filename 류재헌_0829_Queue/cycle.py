import sys
sys.stdin = open('cycle.txt')

for T in range(1, int(input())+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(M):
        arr.append(arr.pop(0))
    print('#{} {}'.format(T, arr[0]))