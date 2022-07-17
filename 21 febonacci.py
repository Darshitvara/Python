def fibo(n):
     a = 0 
     b = 1
     c = 0
     if n < 1:
          print("Enter Valid Input.")
     else:
          if n == 1:
               print(a)
          else:
               print(a,b,end=' ')
               for i in range(2,n):              
                    c = a + b
                    print(c,end=' ')          
                    a = b
                    b = c
                    c = 0
          globals()['flag'] = 1
flag = 0         
while flag == 0:    
     print("Enter Range : ",end='')
     rng = int(input())
     fibo(rng)

