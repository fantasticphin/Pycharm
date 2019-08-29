import sys
sys.stdin = open('Miro.txt')

def initiate():
    for i in range(n):
        for j in range(n):
            if bax[i][j] == '2':
                return (i,j)

def bobo():
    global depth
    while qu:
        a = qu.pop(0)
        i, j, d = a[0][0], a[0][1], a[1]
        if d > depth:
            depth +=1
        if bax[i][j] == '3':
            return True
        bax[i][j] = '1'
        for delta in [1, -1]:
            if i + delta >= 0 and i + delta < n:
                if bax[i+delta][j] != '1':
                    qu.append(([i+delta, j], depth + 1))
            if j + delta >= 0 and j + delta < n:
                if bax[i][j+delta] != '1':
                    qu.append(([i, j+delta], depth + 1))
    return False

for t in range(1, int(input())+1):
    n = int(input())
    bax = [list(input())for _ in range(n)]
    depth = -1
    ints = initiate()
    qu = [([ints[0], ints[1]], -1)]
    if not bobo():
        depth = 0
    print('#{} {}'.format(t, depth))
