for t in range(1, int(input())+1):
    a = list(map(int, input().split()))
    p = a[0]
    q = a[1]
    r = a[2]
    s = a[3]
    w = a[4]
    asol = w*p
    if w <= r:
        bsol = q
    else:
        bsol = q+(w-r)*s
    sol = asol if asol < bsol else bsol
    print('#{} {}'.format(t, sol))
