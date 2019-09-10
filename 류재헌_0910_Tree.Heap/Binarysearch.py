import sys
sys.stdin = open('Binarysearch.txt')
def in_tra(i):
    global num
    if i <= N:
        in_tra(i * 2)
        tree[i] = num
        num += 1
        in_tra(i*2+1)
for tc in range(1,int(input())+1):
    N = int(input())
    num = 1
    tree = [0 for _ in range(N+1)]
    in_tra(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))