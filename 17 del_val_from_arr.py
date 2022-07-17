
from array import *

arr = array("i",[23,33,4,5,43])

print("Enter index from array : ",end='')
n = int(input())

for i in range(len(arr)):
     if i == n - 1 :
          continue
     print(arr[i])