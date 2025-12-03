# K,S=map(int,input().split())
# lst=[]
# count=0
# for i in range(K+1):
#     for j in range(K+1):
#         for k in range(K+1):
#             lst.append([i,j,k])
# for i in lst:
#     if(i[0]+i[1]+i[2]==S):
#         count+=1
# print(count)

K, S = map(int, input().split())
count = 0

for i in range(K+1):
    for j in range(K+1):
        k = S - i - j
        if 0 <= k <= K:
            count += 1

print(count)
