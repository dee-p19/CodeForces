S=input()
N=int(input())
lst=list(map(int,input().split()))
for i in lst:
    if(S=='+'):
        print('+'*i) 
    if(S=='*'):
        print('*'*i) 
    if(S=='/'):
        print('/'*i)    
    if(S=='-'):
        print('-'*i)   
