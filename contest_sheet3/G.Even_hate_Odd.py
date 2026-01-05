t=int(input())
l1=[]
l2=[]
for i in range(t):
    l1.append(int(input()))
    l2.append(list(map(int,input().split())))
for i in l2:
    even = 0
    odd = 0
    if(len(i) % 2 != 0):
        print("-1")
        continue
    else:
        for j in i: 
            if(j % 2 == 0):
             even += 1
            else:
             odd +=1
        if(even == odd):
           print("0")
        else:
            mini = min(odd,even)
            print(len(i)//2 - mini)


         
        
            