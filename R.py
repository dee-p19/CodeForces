N=int(input())
y=N//365
N=N%365
m=N//30
N=N%30
print(f"{y} years")
print(f"{m} months")
print(f"{N} days")

