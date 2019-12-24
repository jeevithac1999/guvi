n=int(input("enter which multiplication table:"))
f=n
while(f>=10):
    f=f//10
l=n%10
print("first digit ",f)
print("last digit ",l)
print("sum = ",f+l)
