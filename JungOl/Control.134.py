a = list(map(int,input().split()))
e = len([x for x in a if x % 2 ==0])
o = len([y for y in a if y %2])
print('even : {}'.format(e))
print('odd : {}'.format(o))