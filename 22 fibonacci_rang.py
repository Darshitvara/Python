def fibo(n):
     a = 0 
     b = 1
     c = 0
     flag = 0
     if n < 0:
          print("Enter Valid Input.")
     else:
          if n == 0 :
               print(a)
          else:                    
               print(a,b,end=' ')
               while flag==0:              
                    c = a + b
                    if c <= n:
                         print(c,end=' ')                         
                         a = b
                         b = c
                         c = 0
                    else:
                         flag=1
                         
print("Enter Range : ",end='')
rng = int(input())
fibo(rng)