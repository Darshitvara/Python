def sub(a,b):
     return a-b

def goodsub(func):

     def inner(x,y):
          if x < y :
               x,y = y ,x 
          return func(x,y)

     return inner

sub = goodsub(sub)   # It can modifiy the function.  must be declared before it's used.

print('Enter first number : ',end='')
n1 = int(input())
print('Enter second number : ',end='')
n2 = int(input())

print(sub(n1,n2))

#sub = goodsub(sub)       It does not affect the function.
