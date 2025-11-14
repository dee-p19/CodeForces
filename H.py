import math as m
A,B=map(int,input().split())
print(f"floor {A} / {B} = {m.floor(A/B)}")
print(f"ceil {A} / {B} = {m.ceil(A/B)}")
print(f"round {A} / {B} = {round(A/B)}")
