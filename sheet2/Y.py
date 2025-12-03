# def fib(n):
#     if(n==1 or n==2):
#         return n-1
#     a=fib(n-1)+fib(n-2)
#     return a

# N=int(input())
# for i in range(1,N+1):
#     print(fib(i),end=" ")



def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

N = int(input())
fib(N)
