<<<<<<< HEAD
# def fib(N):
#   if(N==1):
#     fibo=0
#   elif(N==2):
#     fibo=1
#   else:
#     fibo= fib(N-1)+ fib(N-2)
#   return fibo

# N=int(input())
# print(fib(N))

def fib(N):
    if N <= 0:
        return 0
    elif N == 1:
        return 0
    elif N == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(3, N + 1):
        # Calculate the next number
        a, b = b, a + b
    
    # b now holds the N-th Fibonacci number
    return b

N = int(input())
print(fib(N))
=======
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
>>>>>>> 464430a6b99620935fd179a9de751edc907c96ca
