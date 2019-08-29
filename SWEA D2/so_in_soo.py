for t in range(int(input())):
    temp = int(input())
    m = [0,0,0,0,0]
    while temp > 1:
        if temp % 2 == 0:
            temp = temp/2
            m[0] += 1
        if temp % 3 == 0:
            temp = temp/3
            m[1] += 1
        if temp % 5 == 0:
            temp = temp/5
            m[2] += 1
        if temp % 7 == 0:
            temp = temp/7
            m[3] += 1
        if temp % 11 == 0:
            temp = temp/11
            m[4] += 1
    m = ' '.join(map(str, m))
    print('#{} {}'.format(t+1, m))