a,b = map(int,input().split())
aa =[]
if a >= b:
    for x in range(b, a+1):
        if x % 3 ==0 or x % 5 == 0:
            aa.append(x)
else:
    if a < b:
        for x in range(a, b + 1):
            if x % 3 == 0 or x % 5 == 0:
                aa.append(x)
aaa = sum(aa)
aaaa = round(aaa/len(aa),1)
print('sum : {}'.format(aaa))
print('avg : {}'.format(aaaa))
