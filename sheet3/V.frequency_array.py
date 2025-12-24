# N,M=map(int,input().split())
# A=list(map(int,input().split()))
# for i in range(1,M+1):
#     freq=A.count(i)
#     print(freq)

# N,M=map(int,input().split())
# A=list(map(int,input().split()))
# for i in range(1,M+1):
#     freq=A.count(i)
#     print(freq)

n, m = map(int, input().split())
arr = list(map(int, input().split()))

freq = [0] * (m + 1)

for x in arr:
    freq[x] += 1

for i in range(1, m + 1):
    print(freq[i])


