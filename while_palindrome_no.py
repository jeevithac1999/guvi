m=int(input("Enter n:"))
n=m
rev=0
while(n>0):
    rev=rev*10+(n%10)
    n=n//10
if(m==rev):
    print(m,'is a palindrome')
else:
    print(m,'is not a palindrome')

