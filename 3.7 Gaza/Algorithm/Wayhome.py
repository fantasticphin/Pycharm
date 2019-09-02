import sys
sys.stdin = open('Wayhome.txt')

def dodo(i):
    global ans
    if ans:
        return
    if i == 99:
        ans = 1
        return
    for j in edge[i]:
        if not visit[j]:
            visit[j] = True
            dodo(j)

while True:
    try: tc, N = map(int,input().split())
    except: break
    arr = list(map(int,input().split()))
    edge = [[]for _ in range(100)]
    visit = [False]*100
    for i in range(N):
        edge[arr[2*i]].append(arr[2*i+1])
    ans = 0
    dodo(0)
    print('#{} {}'.format(tc, ans))