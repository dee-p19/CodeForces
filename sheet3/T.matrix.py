N=int(input())
A=[]
for i in range(N):
    A.append(list(map(int,input().split())))
sum1=0
sum2=0
for i in range(N):
    sum1+=A[i][i]
    sum2+=A[i][-i-1]
print(abs(sum1-sum2))
