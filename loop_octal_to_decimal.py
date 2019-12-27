num=int(input('Enter an octal number : '))
dec_value=0; 
base=1; 
temp=num; 
while(temp): 
    last=temp%10; 
    temp//=10; 
    dec_value+=last*base; 
    base*=8; 
print(dec_value)
