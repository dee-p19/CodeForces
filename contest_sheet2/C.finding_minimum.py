# N,K=map(int,(input().split()))
# lst=[]
# temp=[]
# lst=list(map(int,input().split()))
# j=0
# for i in lst:
#     temp.append(i)
#     j+=1
#     if(j<K):
#         continue
#     print(min(temp),end=" ")
#     temp.clear()
#     j=0
# if(len(temp)<K):
#   print(min(temp))
   
N, K = map(int, input().split())
lst = list(map(int, input().split()))

temp = []

for x in lst:
    temp.append(x)
    if len(temp) == K:     # group completed
        print(min(temp), end=" ")
        temp = []          # reset group

# If leftover elements exist (size < K)
if temp:
    print(min(temp), end=" ")

