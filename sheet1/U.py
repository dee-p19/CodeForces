N=(input())
if '.' in N:
    integer ,decimal=N.split(".")
    if(int(decimal)==0):
        print(f"int {integer}")
    else:
        print(f"float {integer} .{decimal}")
else:
    print(f"integer {N}")