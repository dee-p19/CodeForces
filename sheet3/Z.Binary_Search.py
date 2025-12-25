N,Q=map(int,input().split())
lst=list(map(int,input().split()))
a=[]
for i in range(Q):
   nput=int(input())
   if (nput in lst):
       a.append("found")
   else:
       a.append("not found")
for i in a:
    print(i)
