import sys
sys.stdin = open('Contact.txt')

def bobo():
    while qu:
        SI = len(qu)
        ans = 0
        for i in range(SI):
            temp = qu.pop(0)
            for j in connect[temp]:
                if not visit[j]:
                    visit[j] = 1
                    qu.append(j)
            if temp > ans:
                ans = temp
    return ans


for tc in range(1, 11):
    V,E = map(int,input().split())
    labs = list(map(int, input().split()))
    connect= [[] for _ in range(101)]
    visit = [0] * 101
    for i in range(0, V, 2):
        connect[labs[i]].append(labs[i+1])
    qu = [E]
    visit[E] = 1
    print('#{} {}'.format(tc, bobo()))
