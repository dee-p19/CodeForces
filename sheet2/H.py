X=int(input())
#for i in range(2,X):
i=2
while(i<X):
    if X%i==0:
        print("NO")
        break
    i+=1
if(i==X):
    print("YES")