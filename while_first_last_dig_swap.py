n=int(input("enter n:"))
f=t=n
m=n
d=-1
while(t>0):
    t=t//10
    d+=1
while(f>=10):
    f=f//10
l=n%10
e=(m-(f*10**d))+(l*10**d)-l+f
print('\noriginal no',n,'\nexchanged:',e)

