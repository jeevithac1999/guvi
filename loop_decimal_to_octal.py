n=int(input("enter number"))
octalNum=[0]*100
i=0 
while (n != 0): 
    octalNum[i] = n % 8 
    n//=8
    i+=1
for j in range(i-1,-1,-1): 
    print(octalNum[j], end = "")
