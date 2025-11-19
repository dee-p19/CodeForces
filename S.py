X=float(input())
if(X>=0 and X<=25):
    print("Interval [0,25]")
elif(X>25 and X<=50):
    print("Interval (25,50]")
elif(X>50 and X<=75):
    print("Interval (50,75]")
elif(X>75 and X<=100):
    print("Interval (75,100]")
else:
    print("Out of Intervals")