<<<<<<< HEAD
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
=======
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
>>>>>>> 464430a6b99620935fd179a9de751edc907c96ca
