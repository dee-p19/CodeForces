A,B=map(int,input().split())
S=input()
def solve():
  if(S[A]!='-'):
      print("No")
      return

  if(len(S)!=A+B+1):
      print("No")
      return
  for i in range(A+B+1):
    if(i==A):
      continue
    if(not S[i].isdigit()):
      print("No")
      return
  print("Yes")

solve()
  