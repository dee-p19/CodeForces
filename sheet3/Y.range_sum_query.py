# N,Q=map(int,input().split())
# lst=list(map(int,input().split()))
# p=[]
# for i in range(Q):
#   p.append(list(map(int,input().split())))
# for i in p:
#   sum=0
#   for j in range(i[0]-1,i[1]):
#      sum+=lst[j]
#   print(sum)

  
# import sys
# input = sys.stdin.readline

# Read N and Q
N, Q = map(int, input().split())

# Read array elements
A = list(map(int, input().split()))

# Build prefix sum array
prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + A[i]

# Store results instead of printing immediately
results = []

# Read all queries
for _ in range(Q):
    L, R = map(int, input().split())
    results.append(prefix[R] - prefix[L - 1])

# Print output after all input is processed
for ans in results:
    print(ans)

  
