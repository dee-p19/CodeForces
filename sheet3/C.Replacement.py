N=int(input())
lst=list(map(int,input().split()))
j=0
for i in lst:
    if(i<0):
        lst[j]=2
    elif(i>0):
        lst[j]=1
    print(lst[j],end=" ")
    j+=1



