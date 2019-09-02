for i in range(int(input())):
    s = 0
    for x in range(1, int(input())+1):
        if x % 2:
            s += x
        else:
            s -= x
    print('#{} {}'.format(i+1, s))