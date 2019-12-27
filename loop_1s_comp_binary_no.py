n=input("Enter a binary number:")
numb=[int(j) for j in n]
for i in range(len(numb)):
    if numb[i] == 0:
        numb[i] = 1
    else:
        numb[i] = 0
for i in numb: 
    print(i, end="") 
