T=int(input())
lst =[]
temp=[]
for i in range(T):
    N=int(input())
    lst.append(list(map(int,input().split())))
for k in range(T):
  count=0
  for i in range(len(lst[k])):
      for j in range(i,len(lst[k])):
        temp.append(lst[k][j])
        if(temp==sorted(temp)):
            count+=1
      temp.clear()
  print(count)

