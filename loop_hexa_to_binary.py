h=input("enter a hexadecimal number:")
n = int(h, 16)  
b='' 
while n>0: 
    b=str(n%2)+b 
    n=n>>1    
print(str(b)) 
