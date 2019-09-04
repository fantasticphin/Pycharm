a = list(map(int,input().split()))
for x in a:
    if x > 100:
        a.pop(-1)
    elif x < 0:
        a.pop(-1)
print('sum : {}'.format(sum(a)))
print('avg : {}'.format(round(sum(a)/len(a), 1)))