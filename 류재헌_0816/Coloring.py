import sys
sys.stdin = open("Coloring.txt")

T = int(input())


# for tc in range(1, T+1):
#     boxes = int(input())
#     cnts = 0
#     data = [list(map(int, input().split())) for _ in range(boxes)]
#     chart = [[0 for x in range(10)] for y in range(10)]
#     print(chart)

for tc in range(T):
   N=int(input())
   cnt=0
   sol=[['0']*10 for _ in range(10)]
   data= [[0]*5for _ in range(N)]
   for i in range(N):
       data[i] = list(map(int,input().split()))
   for i in range(N):
       for j in range(data[i][0],data[i][2]+1):
           for k in range(data[i][1],data[i][3]+1):
               sol[j][k] +=str(data[i][4])
   for i in range(10):
       for j in range(10):
           if '1' in sol[i][j] and '2' in sol[i][j]:
               cnt+=1
   print("#{} {}".format(tc+1,cnt))