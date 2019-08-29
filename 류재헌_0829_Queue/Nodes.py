import sys
sys.stdin = open('Nodes.txt')

def bobo():
    global N
    if S == G:
        return
    while que:
        size = len(que)
        N += 1
        for i in range(size):
            temp = que.pop(0)
            for j in connect[temp]:
                if visit[j] == 1:
                    continue
                visit[j] = 1
                que.append(j)
        if G in que:
            return
    N=0


for t in range(1, int(input())+1):
    V,E = map(int,input().split())
    connect = [[] for _ in range(V+1)]
    visit = [0] * (V+1)
    for i in range(E):
        x,y = map(int,input().split())
        connect[x].append(y)
        connect[y].append(x)
    S,G = map(int, input().split())
    que = [S]
    visit[S] = 1
    N = 0
    bobo()
    print('#{} {}'.format(t,N))
