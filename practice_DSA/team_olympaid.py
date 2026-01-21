n = int(input())
lst = list(map(int,input().split()))
c1=[]
c2=[]
c3=[]
for i in range(len(lst)):
  if(lst[i]==1):
    c1.append(i)
  elif lst[i]==2:
    c2.append(i)
  else:
    c3.append(i)
m = min(len(c1),len(c2),len(c3))
print(m) 
for i in range(m):
  print(c1[i]+1,c2[i]+1,c3[i]+1)
  
  