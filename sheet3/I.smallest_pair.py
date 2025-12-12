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



