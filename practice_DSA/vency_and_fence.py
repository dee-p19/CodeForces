n,h = map(int,input().split())
lst=list(map(int,input().split()))
ans = 0
for i in lst:
    if(i > h):
        ans += 2
    else:
        ans += 1
print(ans)