N,M=(map(int,input().split()))
lst=[]
for i in range(N):
    lst.append(list(input().split()))
X,Y=map(int,input().split())

def check(x,y):
        if(x<N and y<M):
            if(lst[x][y]!='x'):
                return 0
            else:
                return 1
        else:
             return 1
            
def call(X,Y):
    a= check(X,Y-1)
    b= check(X,Y+1)
    c= check(X-1,Y)
    d= check(X-1,Y-1)
    e= check(X-1,Y+1)
    f= check(X+1,Y)
    g= check(X+1,Y-1)
    h= check(X+1,Y+1)
    if(a!=1 or b!=1 or c!=1 or d!=1 or e!=1 or f!=1 or g!=1 or h!=1):
         return 0
    else:
         return 1       

if(call(X-1,Y-1) ==0):
     print("no")
else:
     print("yes")