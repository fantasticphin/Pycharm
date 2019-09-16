import sys
sys.stdin = open('Binary_Passcode.txt')
def confirm(D):
    global temp
    for y in range(n):
        for x in range(m-1,-1,-1):
            if D[y][x] == '1':
                for z in range(56):
                    temp.append(int(D[y][x-z]))
                return

lis = [[0,0,0,1,1,0,1], [0,0,1,1,0,0,1], [0,0,1,0,0,1,1], [0,1,1,1,1,0,1],
      [0,1,0,0,0,1,1], [0,1,1,0,0,0,1],[0,1,0,1,1,1,1], [0,1,1,1,0,1,1],
      [0,1,1,0,1,1,1], [0,0,0,1,0,1,1]]

for tc in range(1, int(input())+1):
    n,m = map(int,input().split())
    D = [list(input())for _ in range(n)]
    temp = []
    confirm(D)
    temp.reverse()

    end = []
    for i in range(0,len(temp), 7):
        Right = []
        for j in range(7):
            Right.append(temp[i+j])
        for k in range(10):
            if Right == lis[k]:
                end.append(k)

    a = (end[0]+end[2]+end[4]+end[6])*3 +end[1]+end[3]+end[5]+end[7]
    print('#{}'.format(tc), end=' ')
    if a % 10:
        print(0)
    else:
        print((end[0]+end[2]+end[4]+end[6])+end[1]+end[3]+end[5]+end[7])