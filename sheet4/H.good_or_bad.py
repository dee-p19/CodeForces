T=int(input())
lst= []
for i in range(T):
    lst.append(input())
for i in lst:
    if('101' in i or '010' in i):
        print("Good")
    else:
        print("Bad")
       
    
            


