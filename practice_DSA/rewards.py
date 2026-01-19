import math

a = list(map(int,input().split()))
b = list(map(int,input().split()))
n = int(input())
sum1 = 0
sum2 = 0
for i in range(3):
    sum1 += a[i]
    sum2 += b[i]
if (math.ceil(sum1/5) + math.ceil(sum2/10) <= n):
    print("YES")
else:
    print("NO")


