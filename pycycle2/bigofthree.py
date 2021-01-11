print("program for finding biggest of three numbers")
a=float(input("enter first no: "))
b=float(input("enter second no: "))
c=float(input("enter third no: "))
if a>b and a>c:
    print(a, "is bigger")
elif b>a and b>c:
    print(b,"is bigger")
else:
    print(c,"is bigger")
