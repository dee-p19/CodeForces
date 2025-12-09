N=int(input())
lst=list(map(int,input().split()))
for i in range(len(lst)):
    print(lst[-i-1],end=" ")