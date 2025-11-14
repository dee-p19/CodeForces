A,B,C=map(int,input().split())
if(A>B and  A>C):
    M=A
elif(B>A and B>C):
    M=B
else:
    M=C

if(A<B and  A<C):
    Mi=A
elif(B<A and B<C):
    Mi=B
else:
    Mi=C
print(f"{Mi} {M}")


 