octal=int(input('Enter an octal number : '))
decimal=0
i=0
binary=0
while(octal != 0):
    decimal+=(octal%10)*8**i
    i+=1
    octal//=10
i=1
while(decimal != 0):
    binary+=(decimal%2)*i
    decimal//=2
    i*=10
print(binary)
