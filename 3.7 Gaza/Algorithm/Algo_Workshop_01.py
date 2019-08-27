import sys
sys.stdin = open("Algo_workshop_01.txt")
T = 10
for tc in range(T): #T까지 돌리면 나중에 Tc에 더해야함
    N = int(input())  #100
    arr = list(map(int, input().split()))

    ans = 0

    for x in range(2, len(arr) - 1):
        z = 255; b = 0
        for i in range(x-2, x+3):
            if i != x:
                if arr[x] < arr[i]:
                    b = 1
                    break
                y = arr[x] - arr[i]
                if y < z:
                    z = y
        if b == 0:
            ans += z

    print("#{} {} ".format(tc+1, ans))