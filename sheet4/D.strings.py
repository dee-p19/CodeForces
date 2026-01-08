A = input()
B = input()

print(len(A), len(B))
print(A + B)

newA = B[0] + A[1:]
newB = A[0] + B[1:]

# a = A.replace(A[0] , B[0])
# b = B.replace(B[0] , A[0])

print(newA, newB)
