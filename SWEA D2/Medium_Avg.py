import sys
sys.stdin = open('Medium_Avg.txt')

N = int(input())
for tc in range(1, N+1):
    a = list(map(int,input().split()))
    a.remove(max(a))
    a.remove(min(a))
    b = sum(a)/len(a)

    print('#{} {}'.format(tc, round(b)))