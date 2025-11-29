T=int(input())
lst=[]
for i in range(T):
    lst.append(input())
for i in lst:
    for j in range(len(i)):
        print(i[-(j+1)],end=' ')
    print()