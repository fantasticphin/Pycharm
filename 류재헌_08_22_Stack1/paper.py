import sys
sys.stdin = open('paper.txt')

def paps(x):
    if x == N:
        return 1
    if x > N:
        return 0
    return paps(x+10) + paps(x+20) * 2

# def f(k):
#     if k <= 1:
#         return 1
#     else:
#         return f(k-1) + 2*f(k-2)

TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    print('#{} {}'.format(tc, paps(0)))