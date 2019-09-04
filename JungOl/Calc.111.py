a = list(map(int,input().split()))

def sums(a):
    return sum(a)
def avs(a):
    return int(sum(a)/len(a))
print('sum {}'.format(sums(a)))
print('avg {}'.format(avs(a)))
