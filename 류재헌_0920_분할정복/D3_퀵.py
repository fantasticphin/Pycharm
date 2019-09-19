import sys
sys.stdin=open('quick_sort.txt')

def quicky(a):
    if len(a) <= 1: return a

    pivot = a[len(a)//2]
    less, cent, great = [], [], []
    for x in a:
        if x < pivot:
            less.append(x)
        elif x > pivot:
            great.append(x)
        else:
            cent.append(x)
    return quicky(less) + cent + quicky(great)

for tc in range(1,int(input())+1):
    N = int(input())
    A = list(map(int,input().split()))
    print(A)
    quicky(A)
    print(A)
    # print('#{} {}'.format(tc, A[int(len(A)/2)]))