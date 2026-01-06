X = input()
Y = input()
for i in range(min(len(X),len(Y))):
    if(X == Y):
        print(X)
        break
    if(X[i] == Y[i]):
        continue
    else:
        if(min(X[i],Y[i]) == X[i]):
            print(X)
        else :
            print(Y)
        break

