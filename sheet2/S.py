T=int(input())
lst=[]
for i in range(T):
    lst.append(list(map(int,input().split())))
for i in lst:
    sum=0
    for j in range(i[0]+1,i[1]):
        if(j%2!=0):
            sum+=j
    print(sum)  