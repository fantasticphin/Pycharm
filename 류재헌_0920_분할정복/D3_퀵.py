import sys
sys.stdin=open('quick_sort.txt')

def part(l,r):
    p = A[r]
    i = l-1
    for j in range(l,r):
        if A[j] <= p:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def sonic(l,r):
    if l < r:
        s = part(l,r)
        sonic(l, s-1)
        sonic(s+1, r)

for tc in range(1,int(input())+1):
    N = int(input())
    A = list(map(int,input().split()))
    sonic(0,N-1)
    print('#{} {}'.format(tc, A[N//2]))


# for tc in range(1,int(input())+1):
#     N = int(input())
#     A = sorted(list(map(int,input().split())))
#     B = A[int(len(A)/2)]
#     print('#{} {}'.format(tc, B))