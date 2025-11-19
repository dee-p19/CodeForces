e=input()
if '+' in e:
    A,B=e.split('+')
    print(int(A)+int(B))
elif '-' in e:
    A,B=e.split('-')
    print(int(A)-int(B))
elif '*' in e:
    A,B=e.split('*')    
    print(int(A)*int(B))
elif '/' in e:
    A,B=e.split('/')
    print(int(A)//int(B))



