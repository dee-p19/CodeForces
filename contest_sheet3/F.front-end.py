# n = int(input())
# a = list(map(int, input().split()))
# while(len(a)>0):
#     print(a[0],end=" ")
#     a.remove(a[0])
#     if(len(a)>0):
#         print(a[-1],end=" ")
#         a.remove(a[-1])
n = int(input())
a = list(map(int, input().split()))
l, r = 0, n - 1
result = []

while l <= r:
    result.append(a[l])
    l += 1
    if l <= r:
        result.append(a[r])
        r -= 1

print(*result)

