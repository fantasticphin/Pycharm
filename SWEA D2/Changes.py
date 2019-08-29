changes = (50000, 10000, 5000, 1000, 500, 100, 50, 10)
for n in range(int(input())):
    t = int(input())
    hand = [0]*8
    for w in changes:
        while t >= w:
            t -= w
            hand[changes.index(w)] += 1
    hand = map(str, hand)
    print('#{}'.format(n+1))
    print(''.join(hand))