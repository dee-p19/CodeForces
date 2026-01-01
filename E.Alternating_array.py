n = int(input())
a = list(map(int, input().split()))

flips_start_positive = 0
flips_start_negative = 0

for i in range(n):
    if i % 2 == 0:  # even index
        if a[i] < 0:
            flips_start_positive += 1
        if a[i] > 0:
            flips_start_negative += 1
    else:  # odd index
        if a[i] > 0:
            flips_start_positive += 1
        if a[i] < 0:
            flips_start_negative += 1

print(min(flips_start_positive, flips_start_negative))
