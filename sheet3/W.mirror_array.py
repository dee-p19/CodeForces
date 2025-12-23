N,M=map(int,input().split())
A=[]
for i in range(N):
  A.append (list(map(int,input().split())))
for i in A:
    i.reverse()
    for j in i:
        print(j,end=" ")
    print()



