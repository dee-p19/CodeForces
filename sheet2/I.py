N=input()
n=len(N)
s=""
temp=""
pallin= False
i=1
while(i<=n):
   s+=N[-i]
   i+=1
if(s==N):
    pallin=True

if s[0]=='0':
  i=1
  while(i<n):  
          temp+=s[i]
          i+=1
  print(temp)
else:
  print(s)
if(pallin==True):
    print("YES")
else:
    print("NO") 


