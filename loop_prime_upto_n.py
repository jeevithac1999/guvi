m=int(input("enter a number:"))
print('Prime numbers upto ',m,' are')
for n in range(2,m+1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)
