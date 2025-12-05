T=int(input())
lst=[]
for i in range(T):
 l,r=map(int,input().split())
 lst.append((l,r))
for l,r in lst:
    if(r<l):
       l,r=r,l
    sum=((r-l+1)*(r+l))//2
    print(sum)
