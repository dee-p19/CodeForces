# l1,r1,l2,r2=map(int,input().slpit())
# if(l1==l2):
#     if(r1>r2):
#         print(f"{l2} {r2}")
#     else:
#         print(f"{l1} {r1}")
        
# elif(l1<l2):
#     if(r1<r2):
#         print(f"{l2} {r1}")
#     else:
#         print(f"{l2} {r2}")
# else


l1, r1, l2, r2 = map(int, input().split())

start = max(l1, l2)
end = min(r1, r2)

if start > end:
    print(-1)
else:
    print(start, end)

