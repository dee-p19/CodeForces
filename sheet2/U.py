N,A,B=map(int,input().split())
sum=0
for i in range(N+1):
  s=0
  j=i
  while(j>=10):
    s=+(j%10)
    j=j//10
  s+=j
  if(s>=A and s<=B):
   sum+=i
print(sum)

