a = list(map(int,input().split()))
b = []
for i in a:
    b.append(i)
    if i == 0:
        b.pop(-1)
print('{} {}'.format(sum(b), int((sum(b)/len(b)))))
