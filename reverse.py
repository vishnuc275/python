x=int(input("enter a number to reverse: "))
rev=0
while(x>0):
    rev =(rev*10)+(x%10)
    x= x// 10
print("reverse of the no. is",rev)