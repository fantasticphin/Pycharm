import sys
sys.stdin=open('D4_선반높이.txt')

def powerset(n, k, ct):      # n: 원소의 갯수, k: 현재depth
    global ans
    if ct >= ans: return
    if n == k:          # Basis Part
        if ct >= H:
            if ans > ct:ans = ct
    else:
        AA[k] = 1
        powerset(n, k + 1, ct + Workers[k])
        AA[k] = 0
        powerset(n, k + 1, ct)

for tc in range(1,int(input())+1):
    W,H = map(int,input().split())
    ans = 987654321
    Workers = list(map(int,input().split()))
    AA = [0] * W
    powerset(W,0,0)
    print('#{} {}'.format(tc, (ans - H)))