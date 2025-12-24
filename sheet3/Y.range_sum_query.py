N,Q=map(int,input().split())
lst=list(map(int,input().split()))
p=[]
for i in range(Q):
  p.append(list(map(int,input().split())))
for i in p:
  sum=0
  for j in range(i[0]-1,i[1]):
     sum+=lst[j]
  print(sum)

  
