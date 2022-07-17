
def f_recursion(x):
     if x == 0:
          return 1
     return x * f_recursion(x-1)


print("Enter Number : ",end='')
n = int(input())
print(f_recursion(n))