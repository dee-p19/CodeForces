N=int(input())
for i in range(N):
    for j in range(N):
        if(j==i and j==N//2):
           print("X",end="")
        elif(j==i):
           print("\\",end="")
        elif(j==N-1-i):
           print("/",end="")
        else:
           print("*",end="")
    print()