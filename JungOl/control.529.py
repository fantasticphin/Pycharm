def obesse(a,b):
    if b + 100 - a > 0:
        return b + 100 - a
    else:
        return b + 100 - a
a,b = map(int,input().split())
if obesse(a,b)>=0:
    print(obesse(a,b))
    print('Obesity')
else:
    print(obesse(a,b))