n = int(input())
worms =list(map(int,input().split()))
m = int(input())
labels =list(map(int,input().split()))
s = 0
sum =[]

for i in worms:
    s += i
    sum.append(s)

for i in labels:
    left = 0
    rig = n-1
    while(left <= rig):
        mid = (left + rig)//2
        if sum[mid] < i:
            left = mid + 1
        else:
            rig = mid - 1
    print(left + 1)  
    # dry run for better understanding for mid + 1