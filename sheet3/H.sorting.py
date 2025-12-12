#bubble sort
N=int(input())
lst=list(map(int,input().split()))
for i in range(N-1):
    for j in range(N-1):
        if(lst[j]>lst[j+1]):
            lst[j],lst[j+1]=lst[j+1],lst[j]
for i in lst:
    print(i,end=' ')
    