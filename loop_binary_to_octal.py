b=int(input("Enter binary number:"))
o=0
dec=0
i=0
while(b!=0):
    dec+=(b%10)*2**i
    i+=1
    b//=10
i=1
while(dec!=0):
    o+=(dec%8)*i
    dec//=8
    i*=10
print(o)
