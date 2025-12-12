N=int(input())
find=False
for i in range(1,):
    for j in range(1,(10**9)+1):
        if(((i**2)+(j**2))%N==0):
            print(f"{i} {j}")
            find=True
            break
    if(find==True):
        break

