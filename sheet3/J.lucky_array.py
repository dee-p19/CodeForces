N=int(input())
lst=list(map(int,input().split()))
c=min(lst)
count=0
for i in lst:
    if i==c:
        count+=1
if(count%2==0):
    print("Unlucky")
else:
    print("Lucky")