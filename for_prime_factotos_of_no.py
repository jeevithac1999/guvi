n = int(input("Enter the number:"))
print("The .prime factors of",n,"are:")
for i in range(1,n+1):
    if n%i==0:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i," is a prime factor of ",n)
