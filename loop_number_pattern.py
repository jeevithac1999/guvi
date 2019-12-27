n=int(input('enter num of rows:'))
for i in range(n): 
    num=1
    for j in range(i+1): 
        print(num,end=" ") 
        num+=1
    print("\r")
