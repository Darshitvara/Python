
import sys

import math

first = sys.argv[1]         # Arguments value

second = sys.argv[2]        # argv is used to take input directly from command prompt.

# index contains values like this : index[0] = filename , index[1] = first argument , index[2] = second argument.
 
# first = input(" Enter first number : ")

# second = input("\n Enter second number : ")

print(" \n Address of fist value          : ",id(first))

print(" \n Address of second value        : ",id(second))   #It is used to find the address of given variables.

print(" \n Addition of given number       : ",int(first) + int(second))

print(" \n Substraction of given number   : ",int(first) - int(second))

print(" \n Multiplication of given number : ",int(first) * int(second))

print(" \n Division of given number       : ",int(first) / int(second))
 
print(" \n Reminder of given number       : ",int(first) % int(second))

print(" \n Power of given number          : ", int(first) ** int(second))

print(" \n squar root of first number     : ",end = ' ')

print(math.sqrt(int(first)),end = ' ')

print("\n\n squar root of second number    : ",end = ' ')

print(math.sqrt(int(second)))