N,M=map(int,input().split())
A=[]
for i in range(N):
  A.append(list(map(int,input().split())))
X=int(input())
found=False
for i in range(N):
 if(X in A[i]):
    found=True
    break
if(found):
  print("will not take number")
else:
  print("will take number")