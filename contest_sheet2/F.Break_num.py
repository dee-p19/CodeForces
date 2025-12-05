N=int(input())
lst=list(map(int,input().split()))
max=0
for i in lst:
  c=0
  while(i%2==0):
    i=i//2
    c+=1
  if(max<c):
    max=c
print(max)