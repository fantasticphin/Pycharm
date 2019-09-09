import sys
sys.stdin = open('Common_ancestor.txt')
def preorder(node):
    if node != 0:
        c.append(node)
        preorder(data[node][0])
        preorder(data[node][1])

for tc in range(1,int(input())+1):
    V,E,v1,v2 = list(map(int,input().split()))
    ancestor = list(map(int,input().split()))
    b1,b2,c = [], [], []
    data = [[0]*3 for _ in range(V+1)]

    for i in range(0, len(ancestor)-1, 2):
        if data[ancestor[i]][0] == 0:
            data[ancestor[i]][0] = ancestor[i+1]
            data[ancestor[i+1]][2] = ancestor[i]
        else:
            data[ancestor[i]][1] = ancestor[i+1]
            data[ancestor[i+1]][2] = ancestor[i]

    while v1 > 1:
        b1.append(data[v1][2])
        v1 = data[v1][2]

    while v2 >= 1:
        b2.append(data[v2][2])
        v2 = data[v2][2]

    if len(b1) >= len(b2):
        for i in range(len(b1)):
            if b1[i] in b2:
                sol = b1[i]
                break
    else:
        for i in range(len(b2)):
            if b2[i] in b1:
                sol = b2[i]
                break

    preorder(sol)
    print('#{} {} {}'.format(tc, sol, len(c)))