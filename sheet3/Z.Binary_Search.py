N,Q=map(int,input().split())
lst=list(map(int,input().split()))
a=[]
for i in range(Q):
    a.append(int(input()))
for i in a:
    if(i in lst):
        print("found")
    else:
        print("not found")