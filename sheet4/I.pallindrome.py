S = input()
palli = True
for i in range(len(S)//2):
    if(S[i] != S[-(i+1)]):
        print("NO")
        palli = False
        break
if(palli):
    print("YES")
