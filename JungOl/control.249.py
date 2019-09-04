A,B = map(int,input().split())

if A >= 7:
    print(int(B * .8))
elif A >= 5:
    print(int(B * .9))
elif A >= 3:
    print(int(B * .95))
