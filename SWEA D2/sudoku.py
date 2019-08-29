def sudoku():
    for a in range(3):
        for b in range(3):
            c = []
            for i in range(3):
                for j in range(3):
                    c.append(n[3*a+i][3*b+j])
            if len(set(c)) != 9:
                return 0
    return 1

for t in range(1, int(input())+1):
    s = 1
    n,c = [], []
    for _ in range(9):
        a = tuple(map(int,input().split()))
        if len(set(a)) == 9:
            n.append(a)
            continue
        s = 0
    if s:
        for x in zip(*n):
            if len(set(x)) == 9:
                continue
            s = 0
    if s:
        s = sudoku()
    print('#{} {}'.format(t,s))