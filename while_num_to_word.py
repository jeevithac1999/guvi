numbers={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}
num=int(input("enter n:"))
l=[]
num_len=len(str(num))-1
while(num_len>0 and num>0):
      if num in numbers and num<1000:
            l.append(numbers[num])
            num_len=0
      elif num<100:
            l.extend([numbers[num-num%10],numbers[num%10]])
            num_len=0
      else:
            q=num//10**num_len
            num=num%10**num_len
            if q!=0:
                l.append(numbers[q])
                l.append(numbers[10**num_len])
            else:
                l.append(numbers[num])
            num_len-=1
print(' '.join(l))
