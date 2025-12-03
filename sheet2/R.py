def ans(x,y):
  if(x<=0 or y<=0):
    return
  sum=0
  for i in range(x,y+1):
    print(i,end=' ')
    sum+=i
  print(f"sum ={sum}")

lst=[]
while(True):
  lst.append(list(map(int,input().split())))
  n=len(lst)
  if(lst[len(lst)-1][0]<=0 or lst[len(lst)-1][1]<=0):
     break

for i in lst:
  if(i[0]>i[1]):
    ans(i[1],i[0])
  else:
    ans(i[0],i[1])




















  


