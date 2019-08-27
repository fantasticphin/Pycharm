import sys
sys.stdin = open("binary.text")

def gyoyeol(a, st, eds, fnd, cnts):
    cnts += 1
    if st > eds:
        return False
    else:
        md_pgs = (st+eds) // 2
        if a[md_pgs - 1] == fnd:
            return cnts
        elif fnd < a[md_pgs - 1]:
            return gyoyeol(a, st, md_pgs, fnd, cnts)
        elif fnd > a[md_pgs - 1]:
            return gyoyeol(a, md_pgs, eds, fnd, cnts)


T = int(input())

for tc in range(T):
    data = list(map(int, input().split()))
    pgs = []
    sol=[]
    for x in range(1, data[0]+1):
        pgs.append(x)
    for y in range(1,3):
        sol.append(gyoyeol(pgs, pgs[0], pgs[-1],data[y],0))
    if sol[0] < sol[1]:
        print('#{} A'.format(tc+1))
    elif sol[0] == sol[1]:
        print('#{} 0'.format(tc+1))
    else:
        print('#{} B'.format(tc+1))