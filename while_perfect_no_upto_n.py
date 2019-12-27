x=int(input("Enter n:"))
print('The perfect numbers upto ',x,'are')
for m in range(1,x+1):
    s=0
    for i in range(1,m):
        if m%i==0:
            s+=i
    if(s==m):
        print(m,'is a perfect number')
