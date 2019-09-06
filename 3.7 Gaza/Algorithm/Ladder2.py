import sys
sys.stdin = open('Ladder2.txt')

for tc in range(1, int(input())+1):
    BD = [list(map(int,input().split()))for _ in range(100)]
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    vis = []
    for i in range(100):
        for j in range(100):
            print(BD[i][j], end=' ')
        print()