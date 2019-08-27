T = int(input())
arr = [1,2,3,4,5,6,7,8,9,10,11,12]
n = len(arr)
for t in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    for i in range(1, 1<<n):
        sum = 0 #cnt 도 적절하게 잘 리셋해야함
        cnt = 0
        for j in range(n+1):
            if i & (1 << j):
                sum += arr[j]
                cnt += 1
        if sum == K and cnt == N:
            ans += 1

    print('#{} {}'.format(t, ans))