N=int(input())
lst=list(map(int,input().split()))
lst2=[]
for i in range(N):
    lst2.append(lst[-1-i])

if(lst==lst2):
   print("YES")
else:
    print("NO")
   
