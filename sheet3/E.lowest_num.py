N=int(input())
lst=list(map(int,input().split()))
mini=min(lst)
print(f"{mini} {lst.index(mini)+1}")