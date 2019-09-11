import sys
sys.stdin = open('Subtree.txt')
#문제 핵심 노드의 개수를 구하는 것
def preorder(node):
    global cnt
    if node != 0:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    tree = [[0 for _ in range(3)] for _ in range(V + 2)]  # left, right, parent
    temp = list(map(int, input().split()))
    cnt = 0

    for i in range(0,len(temp),2):
        if tree[temp[i]][0] == 0:tree[temp[i]][0] = temp[i+1]
        else:tree[temp[i]][1] = temp[i+1]

    preorder(E)
    print('#{} {}'.format(tc, cnt))