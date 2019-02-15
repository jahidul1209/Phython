Number=int(input("Enter Number:"))
if Number > 1:
    for i in range (2,Number):
        if(Number%2==0):
            print(Number,"is Not a Prime Number")
            break
        else:
            print(Number,"is a Prime Number" )
else:
    Print (Number, "it is Negetive Number")
