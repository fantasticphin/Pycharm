a,b = map(int,input().split())
def calc(a,b):
    if a + b != 0:
        return 1
    else:
        return 0

def multi(a,b):
    if a * b != 0:
        return 1
    else:
        return 0

print(calc(a,b), multi(a,b))