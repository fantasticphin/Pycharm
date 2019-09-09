import sys
sys.stdin = open('In_order.txt')
# def inorder(node):
#     if node != 0:
#         preorder(tree[node][0])
#         print('{}'.format(node), end=' ')
#         preorder(tree[node][1])
def inod(i):
    try: inod(edges[int(i)][0])
    except: pass
    print(nod[int(i)], end='')
    try: inod(edges[int(i)][1])
    except: pass

for tc in range(1, 11):
    N = int(input())
    nod = [0]*(N+1)
    edges = [[]for _ in range(N+1)]
    info = [list(input().split())for _ in range(N)]
    for i in info:
        nod[int(i[0])] = i[1]
        edges[int(i[0])].extend(i[2:])
    print('#{} '.format(tc), end=' ')
    inod('1')
    print()

# def inorder(node):
#     if node != 0:
#         inorder(tree[node][0])
#         print('{}'.format(node), end=' ')
#         inorder(tree[node][1])
#
# for tc in range(1, 11):
#     V = int(input())
#     tree = [[0for _ in range(3)]for _ in range(V+1)]
#     temp = list(input().split())
#
#     for i in range(V+1):
#         n1 = temp[i * 2]
#         n2 = temp[i * 2 + 1]
#         if not tree[int(n1)][0]:
#             tree[int(n1)][0] = n2
#         else:
#             tree[int(n1)][1] = n2
#         tree[int(n1)][2] = n1
#     print('{}'.format(tc))
