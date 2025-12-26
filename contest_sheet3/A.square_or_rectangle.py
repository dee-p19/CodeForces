t=int(input())
lst=[]
for i in range(t):
  lst.append(list(map(int,input().split())))
for i in lst:
  if(i[0]==i[1]):
    print("Square")
  else:
    print("Rectangle")

