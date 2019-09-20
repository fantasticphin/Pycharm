import sys
sys.stdin = open('병합정렬.txt')
def merger(l,r):
    i,j = 0,0
    rst = []
    while len(l) > i or len(r) > j:
        if len(l) > i and len(r) > j:
            if l[i] < r[j]:
                rst.append(l[i])
                i += 1
            else:
                rst.append(r[j])
                j += 1
        elif len(l) > i:
            rst.append(l[i])
            i += 1
        elif len(r) > j:
            rst.append(r[j])
            j+= 1
    return rst

def m_s(m):
    global ct
    if len(m) == 1: return m

    mid = len(m)//2

    l = m[0:mid]
    r = m[mid:len(m)]

    l = m_s(l)
    r = m_s(r)

    if l[-1] > r[-1]:
        ct += 1
    return merger(l,r)

for tc in range(1, int(input())+1):
    N = int(input())
    soso = list(map(int,input().split()))
    ct = 0
    a = m_s(soso)
    print('#{} {} {}'.format(tc, a[N//2], ct))
