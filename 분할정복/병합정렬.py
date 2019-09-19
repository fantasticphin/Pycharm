# def merges(m):
#     if len(m) == 1: return m
#
#     correction,correction2 = [],[]
#     mid = len(m) / 2
#     for x in m
#
#
#
# M = [69, 10, 30, 2, 16, 8, 31, 22]
# merges(M)
# print(M)

# def partition(p,L,R):
#     p = A[0]
#     while i < j:
#         while A[i] <= p: i += i
#         while A[j] >= p: j -= j
#         if i < j:
#             A[i],A[j] = A[j],A[i]
#     return j

# A = [11, 45, 23, 81, 28, 34]
A = [11, 45, 22, 81, 23, 34, 99, 17, 8]
# A = [1,1,1,1,1,0,0,0,0,0]
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             lesser_arr.append(num)
#         elif num > pivot:
#             greater_arr.append(num)
#         else:
#             equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
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


# def quick_sort(arr):
#     def sort(low, high):
#         if high <= low:
#             return
#
#         mid = partition(low, high)
#         sort(low, mid - 1)
#         sort(mid, high)
#
#     def partition(low, high):
#         pivot = arr[(low + high) // 2]
#         while low <= high:
#             while arr[low] < pivot:
#                 low += 1
#             while arr[high] > pivot:
#                 high -= 1
#             if low <= high:
#                 arr[low], arr[high] = arr[high], arr[low]
#                 low, high = low + 1, high - 1
#         return low
#
#     return sort(0, len(arr) - 1)

# print(빠정(A))

#이진 검색