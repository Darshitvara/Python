
a = 10
print(a)
print(id(a))  #address of a.

b = a 
print(b)
print(id(b))  #address of b.

a = 8 
print(a)
print(id(a)) #address of a will be changed.   if, we re-assign the value to a.

print(b)
print(id(b))  #Here, twist is that variable b is still holding the value of a which is declared above.
               # So address of b is store same address as a.