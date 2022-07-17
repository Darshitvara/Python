while(1):
     
     try :
         uip = int(input("Enter Number : "))
         if uip > 100 :
               break
     except Exception as invalid_input :
          print(invalid_input)
          break 
     
print(" Done.")