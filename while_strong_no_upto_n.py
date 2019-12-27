x=int(input("Enter n:"))
print('The perfect numbers upto ',x,'are')
for m in range(1,x+1):
    s=0
    t=m
    fact=1
    while(m!=0):
        rem=m%10
        for i in range(2,rem+1):
            fact*=i
        s+=fact
        m=m//10
        fact=1
    if(t==s):
        print(t,"is a strong number")
