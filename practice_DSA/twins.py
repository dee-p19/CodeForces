N= int(input())
lst=(list(map(int,input().split())))
lst.sort(reverse=True)
total = sum(lst)
sum = 0
count = 0
for i in lst:
    sum += i
    count +=1
    if(sum > total-sum):
        print(count)
        break
 

