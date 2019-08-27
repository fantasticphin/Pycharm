def binsearch(a, key, page):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        middle = (start+end) // 2
        cnt += 1
        if key == a[middle]:
            return cnt
        elif key < a[middle]:
            end = middle
        else:
            start = middle



T = int(input())
arr = [0] * 1001
for i in range(1, 1001):
    arr[i] = i

for tc in range(1, T+1):
    ans = 0
    P, A, B = map(int, input().split())