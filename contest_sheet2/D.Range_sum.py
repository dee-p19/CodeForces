T=int(input())
lst=[]
for i in range(T):
 lst.append(list(map(int,input().split())))
for i in lst:
    sum=0
    for j in range(i[0],i[1]+1):
        sum+=j
    print(sum)