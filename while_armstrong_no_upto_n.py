x=int(input("Enter n:"))
print('The armstrong numbers upto ',x,'are')
for m in range(1,x+1):
    n=m
    s=0
    while(n>0):
        d=n%10
        s+=d**3
        n=n//10
    if(m==s):
        print(m)


