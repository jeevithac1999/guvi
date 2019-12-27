h=input("enter a hexadecimal number:")
n = int(h, 16)  
b='' 
while n>0: 
    b=str(n%2)+b 
    n=n>>1    
num=int(str(b))

dec=0
base=1
temp=num
while(temp): 
    l=temp%10
    temp//=10 
    dec+=l*base
    base*=2; 
print(dec) 
