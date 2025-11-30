T=int(input())
lst=[]
bin=[]
for i in range(T):
 lst.append(int(input()))
for i in lst:
 count=0
 ans=0
 while(i>0):
  bin.append(i%2)
  i=i//2
 for i in bin:
  if(i==1):
   count+=1
 bin.clear()
 for i in range(count):
  ans+=2**i
 print(ans)



