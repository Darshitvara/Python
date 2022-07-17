
while(True):

     num1 = int(input("\nEnter first Number  : "))

     num2 = int(input("\nEnter second Number : "))

     oper = input("\nEnter operator      : ")

     if oper == "+":
          print('\t')
          print(num1 , " + ",num2 , " = ", num1+num2)

     elif oper == "-":
          print('\t')
          print(num1 , " - ",num2 , " = ", num1-num2)

     elif oper == "*":
          print('\t')
          print(num1 , " * ",num2 , " = ", num1*num2)

     elif oper == "/":
          print('\t')
          print(num1 , " / ",num2 , " = ", num1/num2)

     elif oper == "%":
          print('\t')
          print(num1 , " % ",num2 , " = ", num1%num2)

     else :

          print('\n\t--Enter valid operator...')

     yo = input("\nEnter Yes if u want to calculate more(y/Y) : ")

     if yo[0] != "y" and yo[0] != "Y" :
          break

print("\nDone.")


