
print(" Enter any string : ", end = " ")
string = input()

print(type(string))  # It will give the type of given variable.

print(len(string))    # It will print the length of given string.

print(string.upper())    # It will print given string in upper order.

print(string.lower())    # It will print given string in lower order.

print(string.capitalize()) # It will print first latter of given string capital.

print(string[ 2 : len(string) : 2])

print(string[ 3  : : 2])  # It will print givan string from 3 to end of string with gap of 2.I

print(string[ : : ])  # It will print whole given string.

print(string[ -2 : -8 : ])    # It will print given string in back an order.

print(string.count("i")) # It will print the number of given character in given string.

print(string.find("ar")) # It will find given character or string in given string and return it's position.

print(string.replace("darshu i","darshit"))  # It will replace the character or string and print.

print(string.isalnum())         # It will print true or false.  
                                # true : if condition true.
                                # false : if condition false.

print(string.isalpha())         # It will print true or false.  
                                # true : if condition true.
                                # false : if condition false.

print(string.endswith("."))     # It will print true or false.  
                                # true : if condition true.
                                # false : if condition false.

print(string.isdecimal()) 

print(string.isdigit()) 

print(string.isupper()) 

print(string.islower())

print(string.encode())


















