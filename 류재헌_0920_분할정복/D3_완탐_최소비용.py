import sys
sys.stdin = open('최소생산.txt')
def factory(i,j,cur_sum):
    global ans
    if ans < cur_sum: return

    if i == j:
        ans = cur_sum
    for x in range(j, i):
        block[j], block[x] = block[x], block[j]
        factory(i,j+1,cur_sum+intro[j][block[j]])
        block[j], block[x] = block[x], block[j]


for tc in range(1, int(input())+1):
    N = int(input())
    intro = [list(map(int,input().split()))for _ in range(N)]
    block = []
    for i in range(N):
        block.append(i)
    ans = 987654321
    cur_sum = 0
    factory(N,0,cur_sum)
    print('#{} {}'.format(tc, ans))