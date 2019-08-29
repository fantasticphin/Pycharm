days = [31,28,31,30,31,30,31,31,30,31,30,31]
for t in  range(int(input())):
    a = list(map(int, input().split()))
    s = sum(days[a[0]-1:a[2]-1])-a[1]+a[3]+1
    print('#{} [}'.format(i+1, s))
