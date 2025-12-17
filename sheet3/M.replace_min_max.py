<<<<<<< HEAD
N=int(input())
lst=list(map(int,input().split()))
maxi=max(lst)
mini=min(lst)
a=lst.index(maxi)
b=lst.index(mini)
lst[a],lst[b]=lst[b],lst[a]
for i in lst:
    print(i,end=" ")
=======
N=int(input())
lst=list(map(int,input().split()))
maxi=max(lst)
mini=min(lst)
a=lst.index(maxi)
b=lst.index(mini)
lst[a],lst[b]=lst[b],lst[a]
for i in lst:
    print(i,end=" ")
>>>>>>> 464430a6b99620935fd179a9de751edc907c96ca
