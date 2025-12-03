T=int(input())
lst=[]

def ans(x,y):  
    sum=0
    for j in range(x+1,y):
        if(j%2!=0):
            sum+=j
    print(sum) 


for i in range(T):
    lst.append(list(map(int,input().split())))
for i in lst:
    if(i[0]>i[1]):
        ans(i[1],i[0])
    else:
        ans(i[0],i[1])

