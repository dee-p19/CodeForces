n = int(input())
lst = list(map(int,input().split()))
sum=0
for i in lst:
    sum += i
a= sum/100
print(a/n*100) 