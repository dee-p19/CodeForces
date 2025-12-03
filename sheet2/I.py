# N=input()
# n=len(N)
# s=""
# temp=""
# pallin= False
# i=1
# while(i<=n):
#    s+=N[-i]
#    i+=1
# if(s==N):
#     pallin=True

# z=0
# while(s[z]=='0'):
#  z+=1
# while(z<n):  
#           temp+=s[i]
#           z+=1
#   print(temp)
# else:
#   print(s)
# if(pallin==True):
#     print("YES")
# else:
#     print("NO") 

N=input()
n=len(N)
s=""
temp=""
pallin= False
i=1

# reverse
while(i<=n):
   s+=N[-i]
   i+=1

# check palindrome
if(s==N):
    pallin=True

# remove ALL leading zeroes (fix)
if s[0]=='0':
  i=0
  # skip all leading zeroes
  while(i<n and s[i]=='0'):
      i+=1
  temp = s[i:]        # remaining part after removing all leading zeros

  if temp=="":        # if all zeros
      temp="0"

  print(temp)
else:
  print(s)

# print YES/NO
if(pallin==True):
    print("YES")
else:
    print("NO")

