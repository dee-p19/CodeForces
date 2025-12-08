N=int(input())
lst=list(map(int,input().split()))
X=int(input())
j=0
for i in lst:
    if(i==X):
        print(j)
        break
    j+=1
if(j==N):
    print('-1')