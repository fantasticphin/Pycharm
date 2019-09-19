def perm(n, k, sum):
    global ans
    if sum <= ans: return  #확률이기 때문에 현재 ans보다 sum이 작으면 1이 아닌 어떤 확률값을 곱해도 더 작아짐.
    if k == n:
        if sum > ans :
            ans = sum
            return
    else:
        for i in range(k, n):
            A[i], A[k] = A[k], A[i]
            perm(n, k+1, sum * data[k][A[k]] / 100)
            A[i], A[k] = A[k], A[i]

import sys
sys.stdin = open("(1865)동철이의일분배_input.txt")
T = int(input())
A = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for tc in range(T):
    ans = 0
    N = int(input())
    data = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        data[i] = list(map(int, input().split()))
    perm(N, 0, 1)
    print("#%d %f" % (tc+1, ans*100))