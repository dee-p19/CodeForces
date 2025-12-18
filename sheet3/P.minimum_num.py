
N=int(input())
lst=list(map(int,input().split()))
c=True
count=0
while(c==True):
    for i in lst:
        if(i%2!=0):
            c=False
            break
    if(c==True):
        for i in range(N):
            lst[i]//=2
        count+=1
           
print(count)
