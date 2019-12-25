n=int(input("Enter n:"))
s=0
while(n>0):
    dig=n%10
    s+=dig
    n=n//10
print(s)
