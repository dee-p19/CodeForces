import math as m
A,B=map(int,input().split())
print(f"floor {A} / {B} = {m.floor(A/B)}")
print(f"ceil {A} / {B} = {m.ceil(A/B)}")
print(f"round {A} / {B} = {m.floor(A/B+0.5)}")

# def floor(a):
#  return int(a)

# def ceil(c):
#  if(c-int(c)==0):
#   return c
#  else:
#   return int(c+1)
 
# def Round(r):
#   if(r-int(r) < int(r)+1-r):
#    return int(r)
#   else:
#    return int(r)+1