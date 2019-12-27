n=int(input("Enter number of terms:"))
n1,n2=0,1
c=0
if(n<=0):
    print("Enter a positive integer")
elif n==1:
    print('Fibonacci sequence upto ',n,':')
    print(n1)
else:
    print('Fibonacci sequence:')
    while c<n:
        print(n1)
        nt=n1+n2
        n1=n2
        n2=nt
        c+=1

