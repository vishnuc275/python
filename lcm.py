def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
a=int(input("enter the value of first number: "))
b=int(input("enter the value of second number: "))
print("The L.C.M. is",compute_lcm(a,b))