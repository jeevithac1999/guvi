m=int(input("enter a number:"))
print('Sum of prime numbers upto ',m,' are')
s=0
for n in range(2,m+1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        s+=n
print(s)
