
age = int(input("Enter Your Age : "))

if age < 5 or age > 70  :
     print("Enter valid age.")
else:
     if age>18 :
          print("You can drive.")
     elif age==18 :
          print("You have to give physical exam for license.")
     else :
          print("You cannot drive.")

