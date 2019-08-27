import sys
sys.stdin = open('IM.middle.avg.txt')

def relay(n):
    n.remove(max(n))
    n.remove(min(n))
    ns = sorted(n)
    npl = sum(ns)
    navg = npl/len(ns)
    return round(navg)

T = int(input())
for tc in range(1, T+1):
    n_data = list(map(int, input().split()))

    print('#{} {}'.format(tc, relay(n_data)))
