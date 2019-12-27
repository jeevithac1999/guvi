n=input("Enter a binary number:")
ln=len(n) 
i=ln-1
while(i>=0): 
    if(n[i]=='1'): 
        break 
    i-=1
if(i==-1): 
    print('1'+n)
k=i-1
while(k>=0): 
    if(n[k]=='1'): 
        n=list(n) 
        n[k]='0'
        n=''.join(n) 
    else: 
        n=list(n) 
        n[k]='1'
        n=''.join(n)   
    k -= 1
print(n)
