a,b = map(int,input().split())
def momo(a,b):
    return divmod(a,b)

print('{} / {} = {}...{}'.format(a,b,*momo(a,b)))