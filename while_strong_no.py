n=int(input("Enter n:"))
s=0
t=n
fact=1
while(n!=0):
    rem=n%10
    for i in range(2,rem+1):
        fact*=i
    s+=fact
    n=n//10
    fact=1
if(t==s):
    print(t,"is a strong number")
else:
    print(t,"is not a strong number")

