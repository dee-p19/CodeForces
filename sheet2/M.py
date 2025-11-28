A,B=map(int,input().split())
check =False
for i in range(A,B+1):
    k=0
    l=len(str(i))
    for j in str(i):
        if(j!='4' and j!='7'):
            break
        k+=1
    if(k==l):
       check=True
       print(i,end=" ")
if(check==False):
    print (-1)
    
 