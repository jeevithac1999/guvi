num=int(input('Enter an octal number : '))
dec_value=0; 
base=1; 
temp=num; 
while(temp): 
    last=temp%10; 
    temp//=10; 
    dec_value+=last*base; 
    base*=8; 
n=dec_value
def changeDigit(d):
    dec=[10,11,12,13,14,15]
    h=["A","B","C","D","E","F"]
    for i in range(7):
        if d==dec[i-1]:
            d=h[i-1]
    return d
hexa=""
while n!=0:
    rem=changeDigit(n%16)
    hexa=str(rem)+hexa
    n//=16
print(hexa)
