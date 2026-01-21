n = int(input())
lst= list(map(int,input().split()))
for i in range(1,n+1):
    print(lst.index(i)+1,end=" ")