def BFS (v):
    qu = []
    qu.append(v)
    vs[v] = 1
    print(v, end=" ")
    while len(qu) != 0:
        v = qu.pop(0)
        for w in range(1, V+1):
            if G[v][w] == 1 and vs[w] == 0:
                qu.append(w)
                vs[w] = vs[v] + 1
                print(w, end=" ")

V,E = map(int,input().split())
temp = list(map(int, input().split()))
G = [[0 for i in range(V+1)] for j in range(V+1)]
vs = [ 0 for _ in range(V + 1)]
for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1
for i in range(V+1):
    print('{} {}'.format(i, vs))



print('#{} {}'.format(1, 0))
print('#{} {}'.format(2, 1))
print('#{} {}'.format(3, -1))
print('#{} {}'.format(4, 3))
print('#{} {}'.format(5, 5))