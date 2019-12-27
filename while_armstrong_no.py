m=int(input("Enter n:"))
n=m
rev=0
while(n>0):
    rev+=(n%10)**3
    n=n//10
if(m==rev):
    print(m,'is a armstrong number')
else:
    print(m,'is not a armstrong number')

