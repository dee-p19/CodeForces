T=int(input())
lst=[]
for i in range(T):
    N=int(input())
    lst.append(list(map(int,input().split())))


for i in lst:
    mini=10**6
    jin=1
    for j in i:
        kin=jin
        for k in range(jin,len(i)):
           sum=0
           sum=j+i[k]+(kin+1)-jin
           if(mini>sum):
             mini=sum
           kin+=1
        jin+=1
    print(mini)
    print(" ")  


