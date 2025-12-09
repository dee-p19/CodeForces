N=int(input())
lst=list(map(int,input().split()))
j=0
for i in lst:
    if(i<=10):
     print(f"A[{j}] = {i}")
    j+=1
    