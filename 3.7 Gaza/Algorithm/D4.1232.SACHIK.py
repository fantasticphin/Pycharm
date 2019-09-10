import sys
sys.stdin = open('Sachik.txt')
def cal(x):
    if nod[x] == '+': return cal(int(edge[x][0])) + cal(int(edge[x][1]))
    elif nod[x] == '-': return cal(int(edge[x][0])) - cal(int(edge[x][1]))
    elif nod[x] == '*': return cal(int(edge[x][0])) * cal(int(edge[x][1]))
    elif nod[x] == '/': return cal(int(edge[x][0])) / cal(int(edge[x][1]))
    else: return int(nod[x])

for tc in range(1,11):
    N = int(input())
    nod = [0 for _ in range(N+1)]
    edge = [[]for _ in range(N+1)]
    for i in range(N):
        info = list(input().split())
        if info[1] in ['+','-','*','/']:
            nod[int(info[0])] = info[1]
            edge[int(info[0])].extend(info[2:])
        else:
            nod[int(info[0])] = info[1]

    print('#{} {}'.format(tc, int(cal(1))))