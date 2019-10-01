def powerset(n, k, cur_weight, cur_val):      # n: 원소의 갯수, k: 현재depth
    global ans
    if cur_weight > W: return

    if n == k:
        if ans < cur_val: ans = cur_val

    else:
        A[k] = 1
        powerset(n, k+1, cur_weight + weight[k], cur_val + value[k])
        A[k] = 0
        powerset(n, k+1, cur_weight, cur_val)

W = 10
n = 4
weight = [5,4,6,3]
value = [10,40,30,50]
A = [0] * n
ans = 0

powerset(n,0,0,0)
print('{}'.format(ans))