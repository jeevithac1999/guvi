num=int(input("Enter binary number:"))
dec=0
base=1
temp=num
while(temp): 
    l=temp%10
    temp//=10 
    dec+=l*base
    base*=2; 
print(dec) 
