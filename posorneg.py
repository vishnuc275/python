x=float(input("enter the no. : "))
if x == 0:
    print(x,"which is neither a negative nor a positive.")
elif x + x >= 0:
    print(x, "is a positive no.")
else:
    print(x, "is a negative no.")