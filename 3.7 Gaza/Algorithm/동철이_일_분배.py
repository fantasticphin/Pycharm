import sys
sys.stdin=open('inputs.txt')

def perm(n, k, m):
    global ans
    if ans >= m:
        return
    if n == k:
        if ans < m:
            ans = m
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            perm(n, k+1, m * data[k][arr[k]])
            arr[i], arr[k] = arr[k], arr[i]

for tc in range(1, int(input())+1):
    N = int(input())
    data = [[int(i)/100 for i in input().split()] for _ in range(N)]
    arr = [i for i in range(N)]
    ans = 0
    perm(N, 0, 1.0)
    print('#{} {:.6f}'.format(tc,ans*100))