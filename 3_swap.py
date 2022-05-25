
a = 10

b = 20

print( " \n Before Swapping ..! ")

print("\n \t A is = ", end='')
print(a, end='')

print("\n \t B is = ", end='')
print(b)

#a,b = b,a

# a = a + b 
# b = a - b
# a = a - b

a = a ^ b                # Using logical XOR gate.
b = a ^ b
a = a ^ b


print( " \n After Swapping ..! ")

print("\n \t A is = ", end='')
print(a, end='')

print("\n \t B is = ", end='')
print(b)
