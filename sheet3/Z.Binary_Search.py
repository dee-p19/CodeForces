# N,Q=map(int,input().split())
# lst=list(map(int,input().split()))
# a=[]
# for i in range(Q):
#    nput=int(input())
#    if (nput in lst):
#        a.append("found")
#    else:
#        a.append("not found")
# for i in a:
#     print(i)



# Read N and Q
N, Q = map(int, input().split())

# Read array and convert to set
A = set(map(int, input().split()))

# Store outputs
results = []

# Read all queries first
for _ in range(Q):
    X = int(input())
    if X in A:
        results.append("found")
    else:
        results.append("not found")

# Print output only after all input is taken
for res in results:
    print(res)
