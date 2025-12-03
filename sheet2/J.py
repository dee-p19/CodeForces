N=int(input())
for i in range(2,N+1):
    t= True
    for j in range(2,i):
        if i%j==0:
            t=False
            break
    if t==True:
        print(i,end=" ")