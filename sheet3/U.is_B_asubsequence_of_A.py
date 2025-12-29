N,M=map(int,(input()).split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
j=0
for i in range(N):
   if(A[i]==B[j]):
      j+=1
   if(j==M):
      break
if(j==M):
   print("YES")
else:
   print("NO")


# N,M=map(int,(input()).split())
# A=list(map(int,input().split()))
# B=list(map(int,input().split()))
# j=0
# for i in range(N):
#    if(A[i]==B[j]):
#       j+=1
#    if(j==M):
#       break
# if(j==M):
#    print("YES")
# else:
#    print("NO")



