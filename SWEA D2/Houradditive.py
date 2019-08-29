import sys
sys.stdin = open('hour.txt')

for t in range(int(input())):
    s = 0
    n = list(map(int, input().split()))
    n[0] += n[2]
    n[1] += n[3]
    if n[1] // 60:
        n[0] += 1
        n[1] %= 60
    n[0] %= 12
    if not n[0]:
        n[0] = 12
    print('#{} {} {}'.format(t+1, n[0], n[1]))