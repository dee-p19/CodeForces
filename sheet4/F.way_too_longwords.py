T=int(input())
lst=[]
for i in range(T):
    lst.append(input())
for i in lst:
    if(len(i) < 10):
        print(i)
    else:
        print(f"{i[0]}{len(i)-2}{i[-1]}")