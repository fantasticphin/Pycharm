import heapq
import sys
sys.stdin = open('Binary_Heap.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    Bin = list(map(int,input().split()))
    correction = []
    # print(Bin)
    for i in Bin:
        heapq.heappush(correction, i)  # (우선순위, 값)
    Bin = [0] + correction
    ans = 0
    cnt = N
    while cnt != 0:
        cnt = cnt // 2
        ans += Bin[cnt]
    print('#{} {}'.format(tc, ans))
