import sys
sys.stdin = open ('division_return.txt')

# def divis(a,b):
#     c = a // b
#     return c
#
# def divisr(a,b):
#     d = a % b
#     return d
#
# T = int(input())
#
# for tc in range(1, T+1):
#     a,b = list(map(int, input().split()))
#     print('#{} {} {}'.format(tc, divis(a,b), divisr(a,b)))

T = int(input())
for tc in range(1, T+1):
    a,b = list(map(int, input().split()))
    c,d = divmod(a,b)
    cs = int(c)
    css = int(d)
    print('#{} {} {}'.format(tc, cs, css))