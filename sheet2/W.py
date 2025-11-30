N=int(input())
sp=0
for i in range(2*N):
    if i<N:
      print(" "*(N-1-sp)+"*"*(1+(2*sp)))
      sp+=1 
    else:
      sp-=1
      print(" "*(N-1-sp)+"*"*(1+(2*sp)))