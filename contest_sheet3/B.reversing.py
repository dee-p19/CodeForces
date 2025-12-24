n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if a[i] == 0:
        # reverse all elements before index i
        a[:i] = reversed(a[:i])

for i in a:
    print(i,end=" ")


