n = int(input())
nn = [ ]
for i in range(1, 101):
    nn.append(i*n)
for j in nn:
    print(j, end=' ')
    if j % 10 == 0:
        break