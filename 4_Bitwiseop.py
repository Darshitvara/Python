
#complement operator

# a = 10                      #  0000 1010   = 10                               
# b = ~a                      #  =========     1's complement
#                             #  1111 0101                         
#                             # +        1     2's complement
# print(b)                    #  =========
#                             #  1111 0110   = -11       

#***********************************************************

# AND operator
# a = 5                          #    0101 = 5
#                                #and 0111 = 7
# b = 7                          #    ====
#                                #    0101 = 5
# c = a & b

# print(c)

#***********************************************************

# OR operator

# a = 8                         #    1000 = 8
#                               # or 1110 = 14
# b = 14                        #    ====
#                               #    1110 = 14
# c = a | b

# print(c)

#***********************************************************

# a = 6                           #     0110 = 6
#                                 # xor 1000 = 8
# b = 8                           #     ====
#                                 #     1110 = 14
# c = a ^ b
 
# print(c)


#***********************************************************

# LEFT SHIFT OPERATOR

# a = 14                             # 1110
#                                    # It's left shift so simply , we'll add zero from right side.
# b = 3                              # Number of adding zero is dependend on b.
#                                    # 1110000
                           
# c = a << 3

# print(c)

#***********************************************************

# RIGHT SHIFT OPERATOR

a = 11                             # 1011 = 11
                                   # It's Right shift so simply , we'll remove binary bits from RIght side.  
b = 2                              # Number of removing binary bits is dependend on b.
                                   # 10 = 2
c = a >> b

print(c)