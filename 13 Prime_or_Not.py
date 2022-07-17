
flag = 0

n = int(input("Enter Number : "))

for i in range(2,n-1):
     if n % i ==  0 :
          flag = 1
          exit 
     
if flag == 1:
     print(n," is Not Prime number.")
else:
     print(n," is Prime number.")
     