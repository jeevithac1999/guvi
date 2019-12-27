m=int(input("Enter n:"))
d=int(input("Enter a digit:"))
c=0
n=m
while(n>0):
	if(n%10==d):
		c+=1
	n//=10
print ("number=",m,"\ndigit=",d,"\nfrequency=",c)
