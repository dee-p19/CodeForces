T=int(input())
lst=[]
temp=[]
for i in range (T):
  N=int(input())
  lst.append(list(map(int,input().split())))
for arr in lst:
  for j in range(len(arr)):
    for k in range(j,len(arr)):
      temp.append(arr[k])
      print(max(temp),end=" ")
    temp.clear()
  print()
      
