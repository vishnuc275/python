x=int(input("enter any number: "))
count=0
while(x>0):
  count=count+1
  x=x//10
print("the number of digits in the given number is: ",count)