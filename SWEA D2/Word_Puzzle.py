import sys
sys.stdin = open('Word_Puzzle.txt')

for i in range(int(input())):
    a,b = map(int,input().split())
    m = [''.join(input().split())for i in range(a)]
    c = [''.join(j) for j in list(zip(*m))]
    z = 0
    for k in [m,c]:
        for j in k:
            x = j.split('0')
            # print(x)
            if '1' * b in x:
                z += x.count('1'*b)
    print('#{} {}'.format(i+1, z))
