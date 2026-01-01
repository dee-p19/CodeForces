n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

max_sum = 0
count = 0

for value in a:
    if count == k or value <= 0:
        break
    max_sum += value
    count += 1

print(max_sum)

