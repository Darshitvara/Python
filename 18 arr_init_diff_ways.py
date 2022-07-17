from numpy import *

arr = linspace(0,12,4)              #    Here, we are creating a array with partition.
                              #   first parameter  : starting of array range
                              #   second parameter : Ending of array range
                              #   third parameter  :  gapp between number 

print(arr)

arr1 = arange(2,21,3)        # Same as linspace()
print(arr1)

arr2 = ones(7)
print(arr2)                   # Creates the array of 1 with given number.

arr3 = zeros(5)
print(arr3)                    # Creates the array of 0 with given number.

arr4 = logspace(5,30,4)
print(arr4)