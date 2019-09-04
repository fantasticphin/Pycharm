A,B = map(int,input().split())
C, D = divmod(A,B)
print('{} * {} + {} = {}'.format(B, C, D, A))