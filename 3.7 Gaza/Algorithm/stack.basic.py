# a = []
# a.append(1)
# a.append(2)
# a.append(3)
# print(a)
# a.pop()
# a.pop()
# a.pop()
# print(a)

# s = list()
# def push(item):
#     s.append(item)
#
# def pop():
#     if len(s) == 0:
#         return
#     else:
#         return s.pop(-1)
#
# def isEmpty():
#     if len(s) == 0: return True
#     else: return False
#
# def check_matching(data):
#     for i in range(len(data)):
#         if data[i] == '(':
#             push(data[i])
#         elif data[i] ==')':
#             if isEmpty(): return False
#             pop()
#     if not isEmpty(): return False
#     else: return True
#
# data = input()
# print(check_matching(data))

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
# print(fact(4))

# def fibo(n):
#     global memoryview
#     if n >= 2 and len(memo) <= n:
#         memo.append(fibo(n-1) + fibo(n-2))
#     return memo[n]
#
# memo=[0,1]

# print(fibo(50))

# def fibo(n):
#     if n == 1 or n == 0:
#         return n
#     else:
#         return (fibo(n-1) + fibo(n-2))
#
# print(fibo(50))

# def fibo_dp(n):
#     f = [0, 1]
#
#     for i in range(2, n+1):
#         f.append(f[i-1] + f[i-2])
#
#     return f[n]
#
# print(fibo_dp(100))

# DFS
# 7 8
# 1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7
# graph = {'1': set(['2', '3']),
#          '2': set(['1', '4', '5']),
#          '3': set(['2', '7']),
#          '4': set(['2', '6']),
#          '5': set(['2', '6']),
#          '6': set(['7', '5'])
#          '7': set(['3'])}
#
# def dfs(graph, start):
#     visited = []
#     stack = [start]
#
#     while stack:
#         n = stack.pop()
#         if n not in visited:
#             visited.append(n)
#             stack += graph[n] - set(visited)
#     return visited
#
# print(dfs(graph, 'A'))

#선생님 방법

def dfs(v):
    visited[v] = 1
    print(v, end='')

    for w in range(V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

V,E = map(int,input().split())
temp = list(map(int, input().split()))

G = [[0 for i in range(V+1)]for j in range(V+1)] #2차원 초기화
visited = [0 for i in range(V+1)]

for i in range(0, len(temp), 2):
    G[temp[i]][temp[1+i]] = 1
    G[temp[i+1]][temp[i]] = 1

for i in range(V+1):
    print('{} {}'.format(i, G[i]))


dfs(1)