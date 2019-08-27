import sys
sys.stdin = open("graph_route.txt")


def dfs(v):
    visited[v] = 1
    tmp = 0
    for w in range(V+1):
        if G[v][w] == 1 and visited[w] == 0:
            if w == ed: return 1
            else:
                tmp = dfs(w)
                if tmp:
                    break
    return tmp

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split()) #정점, 간선
    temp = []
    for _ in range(E):
        temp += list(map(int, input().split()))
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]#이차원 초기화
    visited = [0 for _ in range(V+1)] #방문 했는지 안 했는지.
    st, ed = map(int, input().split())
    for i in range(0,len(temp),2):#입력
        G[temp[i]][temp[i+1]] = 1

    print('#{} {}'.format(tc, dfs(st)))


