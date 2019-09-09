import sys
sys.stdin = open('Tree_Basic.txt')
# def preo_traverse(T): #전위
#     if T:
#         vis(T)
#         preo_traverse(T.L)
#         preo_traverse(T.R)
#
# def ino_traverse(T): #중위
#     if T:
#         ino_traverse(T.L)
#         vis(T)
#         ino_traverse(T.right)
# def poso_traverse(T): #후위
#     if T:
#         poso_traverse(T.L)
#         poso_traverse(T.R)
#         vis(T)

def preorder(node):
    if node != 0:
        print('{}'.format(node), end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node != 0:
        preorder(tree[node][0])
        print('{}'.format(node), end=' ')
        preorder(tree[node][1])

def postorder(node):
    preorder(tree[node][0])
    preorder(tree[node][1])
    print('{}'.format(node), end=' ')

def printTree():
    for i in range(1, V+1):
        print('%2d %2d %2d %2d'.format(i, tree[i][0], tree[i][1], tree[i][2]), end=' ')

V,E = map(int,input().split())
tree = [[0for _ in range(3)]for _ in range(V+1)]
temp = list(map(int,input().split()))

for i in range(E):
    n1 = temp[i * 2]
    n2 = temp[i * 2 + 1]
    if not tree[n1][0]:
        tree[n1][0] = n2
    else:
        tree[n1][1] = n2
    tree[n1][2] = n1

# printTree()

print('pre-order : ', end= '')
preorder(1)
print()

print('inorder : ', end='')
inorder(1)
print()

print('postorder :', end='')
postorder(1)
print()