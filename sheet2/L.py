A,B=map(int,input().split())
if A>B:
    ans=B
else:
    ans=A
for i in range(1,ans+1):
    if A%i==0 and B%i==0:
        ans=i
print(ans)