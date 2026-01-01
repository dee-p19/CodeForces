n, m = map(int, input().split())
arr = list(map(int, input().split()))

freq = [0] * (m + 1)

for x in arr:
    freq[x] += 1

for i in range(1, m + 1):
    print(freq[i])

