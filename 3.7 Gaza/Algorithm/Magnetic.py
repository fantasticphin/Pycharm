import sys
sys.stdin = open('Magnetic.txt')

for t in range(10):
    n = int(input())
    bd = [list(map(int, input().split()))for _ in range(n)]
    a = 0
    for i in range(n):
        k = 0
        for j in range(n):
            if bd[j][i] == 1:
                k = 1
            if bd[j][i] == 2 and k == 1:
                k = 0
                a += 1
    print('#{} {}'.format(t+1, a))