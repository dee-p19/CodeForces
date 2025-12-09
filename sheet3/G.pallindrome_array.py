N=int(input())
lst=list(map(int,input().split()))
for i in range(N//2):
    if(lst[i]!=lst[-i-1]):
     print("NO")
     break
if(i==N//2):
   print("YES")
   
