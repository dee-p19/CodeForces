N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
check=True
for i in range(N):
    if(B[i]!=A[i]):
     check=False
     break
if(check):
   print("yes")
else:
   print("no")