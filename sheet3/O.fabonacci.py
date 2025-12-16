def fib(N):
  if(N==1):
    fibo=0
  elif(N==2):
    fibo=1
  else:
    fibo= fib(N-1)+ fib(N-2)
  return fibo

N=int(input())
print(fib(N))
