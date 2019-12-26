x= int(input("Enter the number1:"))
y= int(input("Enter the number2:"))
if x>y:
    g=x
else:
    g=y
while(1):
    if((g%x==0) and (g%y==0)):
        lcm=g
        break
    g+=1
print("The LCM is",lcm)
