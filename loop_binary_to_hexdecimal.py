num=int(input("Enter binary number:"))
hdec=0
base=1
temp=num
while(temp): 
    l=temp%10
    temp//=10 
    hdec+=l*base
    base*=2; 
print("Equivalent Hexadecimal Number is") 

n=hdec
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
