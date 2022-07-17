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
                         print(c,end='  ')                         
                         a = b
                         b = c
                         c = 0
                    else:
                         flag=1

def f_recursion(x):
     if x == 0:
          return 1
     return x * f_recursion(x-1)

def factorial(x):
     fact = 1
     if x < 1:
          print("Enter valid number.")
     else:
          while x > 0:
               fact = fact * x
               x -= 1
          return fact

def pri():
     print("This function is calling from ",__name__)
  
          #             __name__ is used to check that if any function of module is coming from 
          #     another program than __name__ will return name of that program or module
          #     where function is calling from.