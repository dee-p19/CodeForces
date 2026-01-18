a1,b1 = map(int,input().split(":"))
a2,b2 = map(int,input().split(":"))

c = a1*60 +b1
d = a2*60 +b2

if(c < d):
    c += 1440  #add 24 hours if next day
ans = c-d

hour = ans//60
min = ans%60 

print(f"{hour:02d}:{min:02d}")
