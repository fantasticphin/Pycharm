x = []
for i in range(1, int(input())+1):
    if k & set(str(i)):
        x.append('-'*sum([str(i).count(j)]))
    else:
        x.append(str(i))
    print(' '.join(x))
