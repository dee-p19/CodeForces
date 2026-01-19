n= int(input())
lst = list(map(int,input().split()))
ma = max(lst)
mi = min(lst)
max_pos = lst.index(ma)
min_pos = n -1 -lst[::-1].index(mi)

swaps = max_pos + (n-1-min_pos)

if(max_pos > min_pos):
    swaps -= 1

print(swaps)

