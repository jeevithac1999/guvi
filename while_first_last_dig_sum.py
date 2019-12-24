n=int(input("enter n:"))
f=n
while(f>=10):
    f=f//10
l=n%10
print("first digit ",f)
print("last digit ",l)
print("sum = ",f+l)
