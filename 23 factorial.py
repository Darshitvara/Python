
def factorial(x):
     fact = 1
     if x < 1:
          print("Enter valid number.")
     else:
          while x > 0:
               fact = fact * x
               x -= 1
          return fact

print("Enter Number : ",end='')
n = int(input())
print(factorial(n))