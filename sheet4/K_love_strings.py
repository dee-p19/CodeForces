N = int(input())
lst =[]
for i in range(N):
    lst.append(list( input().split()))
for i in lst:
    # n = max(len(i[0]) , len(i[1]))
    if(len(i[0]) > len(i[1])):
        m = i[0]
        mi = i[1]
    else:
        m = i[1]
        mi = i[0]
    for j in range(len(m)):
        if j < len(mi):
            print(f"{i[0][j]}{i[1][j]}",end="")
        else:
            print(m[j],end="")
    print()
