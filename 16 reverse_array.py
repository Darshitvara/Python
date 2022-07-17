# Print array elements in reverse order without using inbuilt function
from array import *

arr = array('i',[23,33,4,5,43])

i=len(arr)

while i > 0 :
     print(arr[i-1])
     i-=1

