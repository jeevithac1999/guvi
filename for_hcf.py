x= int(input("Enter the number1:"))
y= int(input("Enter the number2:"))
if x>y:
    smaller=y
else:
    smaller=x
for i in range(1,smaller+1):
    if((x%i==0) and (y%i==0)):
        hcf=i 
print("The HCF is",hcf)
