# T=int(input())
# lst=[]
# for i in range(T):
#     N=int(input())
#     lst.append(list(map(int,input().split())))
# for i in lst:
#     mini=10**6
#     for j in range(N):
#         for k in range(j+1,len(i)):
#            sum=0
#            sum=j+i[k]+(kin+1)-jin
#            if(mini>sum):
#              mini=sum
#            kin+=1
#         jin+=1
#     print(mini)
#     print(" ") 


T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    mini = float('inf')

    for i in range(N):
        for j in range(i+1, N):
            value = A[i] + A[j] + (j - i)
            if value < mini:
                mini = value

    print(mini)



