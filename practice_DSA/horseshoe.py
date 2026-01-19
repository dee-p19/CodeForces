lst = list(map(int,input().split()))
temp =[]
count = 0
for i in lst :
    if i in temp:
        count += 1
        continue
    temp.append(i)
print(count)
    
