T=int(input())
# f=1
lst=[]
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
for i in range(T):
  lst.append(int(input()))
for i in lst:
   print(fact(i))