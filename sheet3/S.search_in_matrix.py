N,M=map(int,input().split())
A=[]
for i in range(N):
  A.append(list(map(int,input().split())))
X=int(input())
if(X in A):
  print("will not take number")
else:
  print("will " \
  "take number")